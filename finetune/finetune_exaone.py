import torch
from datasets import Dataset
from Grammar.grammar_ver1_1_4 import grammar
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from peft import LoraConfig, prepare_model_for_kbit_training
from trl import SFTTrainer, SFTConfig

def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
    return { "text" : texts, }
pass

######################################################################################
def extract_classes_by_name(text: str):
    # pattern = r'class\s+(\w+)\s*:\s*\n\s+"""(.*?)"""'
    pattern = r'Device\s+(\w+)\s*:\s*\n\s+"""(.*?)"""'
    matches = re.finditer(pattern, text, re.DOTALL)

    class_dict = {}
    for match in matches:
        class_name = match.group(1)
        full_class_def = match.group(0)  # 전체 클래스 문자열
        class_dict[class_name] = full_class_def

    return class_dict

with open("./ServiceExtraction/integration/service_list_ver1.1.7.txt", "r") as f:
    service_doc = f.read()
classes = extract_classes_by_name(service_doc)

def read_yaml(data):
    dic = {}
    dic['command'] = data['command']
    dic['devices'] = data['devices']
    s = ""
    sub = []
    for i in data['code']:
      k = ""
      k += f"name = \"{i['name']}\"\n"
      k += f"cron = \"{i['cron']}\"\n"
      k += f"period = {i['period']}\n"
      k += i['code'].strip() + "\n"
      sub.append(k)
    s += "---\n".join(sub)
    dic["code"] = s
    return dic

# 데이터셋 생성 부분 수정
def load_dataset():
    ret = []
    for i in range(0, 16):  # 범위를 필요에 따라 조정
        file_name = f"./Testset/TestsetWithDevices/category_{i}.yaml"
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
            for item in data:
                result = read_yaml(item)
                service_doc = "\n".join([classes[device] for device in result['devices'] if device in classes])
                ret.append({
                    "conversations": [
                        {
                            "role": "system",
                            "content": grammar,
                        },
                        {
                            "role": "system", 
                            "content": service_doc,
                        },
                        {
                            "role": "user",
                            "content": f"Generate JOI Lang code for \"{result['command']}\"",
                        },
                        {
                            "role": "assistant",
                            "content": result['code'],
                        }
                    ]
                })
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {file_name}")
        except Exception as e:
            print(f"데이터 처리 중 오류: {e}")
    
    return ret

# 커스텀 데이터셋 생성
data_set = load_dataset()
MY_DATASET = Dataset.from_list(data_set)

# 포매팅 적용
MY_DATASET = MY_DATASET.map(
    formatting_prompts_func,
    batched=True,
    batch_size=32,
    remove_columns=["conversations"]
)

# 4. 양자화 설정
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)

# 5. 모델 & 토크나이저 로드
model_name = "LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct"  # 다른 모델로 교체 가능
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token  # 패딩 토큰 설정

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
)

# 6. 모델 양자화 준비
model = prepare_model_for_kbit_training(model)

# 7. LoRA 설정
peft_config = LoraConfig(
    r=16,  # LoRA 랭크
    lora_alpha=32,
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["q_proj", "v_proj"]
)

# 10. 학습 설정
training_args = SFTConfig(
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    optim="paged_adamw_8bit",
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    max_steps=100,  # 전체 스텝 수
    save_strategy="steps",
    logging_steps=10,
    output_dir="./results",
    report_to="none",
    max_seq_length=1024,  # 모델 최대 길이에 맞춤
)

# 11. 트레이너 초기화
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=MY_DATASET,
    peft_config=peft_config,
    formatting_func=formatting_prompts_func,
    dataset_text_field="text",  # 데이터셋 텍스트 필드 이름
)

# 12. 학습 실행
trainer.train()

# 13. 모델 저장
model.save_pretrained("./final_model")
tokenizer.save_pretrained("./final_model")

# 14. (선택) LoRA 가중치 병합 및 추론
from peft import PeftModel

# 기본 모델 재로드
base_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
)
merged_model = PeftModel.from_pretrained(base_model, "./final_model")
merged_model = merged_model.merge_and_unload()

# 추론 예시
inputs = tokenizer("### 리뷰:\n이 영화는 정말...", return_tensors="pt").to("cuda")
outputs = merged_model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))