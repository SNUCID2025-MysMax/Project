import torch
from datasets import Dataset
from transformers import (
    AutoConfig,
    AutoModelForCausalLM, 
    AutoTokenizer, 
    TrainingArguments, 
    Trainer, 
    DataCollatorForLanguageModeling
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import os
import subprocess

# 1. 데이터 준비
data_all = [
    [
        {
            "from": "human",
            "value": "Input: 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light).on()"
        }
    ],
    # 여기에 더 많은 데이터 추가
]

# 데이터를 변환하여 Dataset 생성
formatted_data = []
for conversation in data_all:
    human_message = next((msg for msg in conversation if msg["from"] == "human"), None)
    gpt_message = next((msg for msg in conversation if msg["from"] == "gpt"), None)
    
    if human_message and gpt_message:
        formatted_data.append({
            "input": human_message["value"],
            "output": gpt_message["value"]
        })

dataset = Dataset.from_list(formatted_data)

# 2. 모델 및 토크나이저 로드
model_name = "LGAI-EXAONE/EXAONE-Deep-2.4B"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 모델 로드 (4비트 양자화 사용)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
    load_in_4bit=True,
)

# 3. LoRA 설정 및 적용
model = prepare_model_for_kbit_training(model)

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj"
    ],
)

model = get_peft_model(model, lora_config)

# 4. 데이터 전처리 함수
def preprocess_function(examples):
    # EXAONE Deep 모델은 <thought>로 시작하는 것이 권장됨
    prompts = []
    for i in range(len(examples["input"])):
        prompt = f"[|user|]{examples['input'][i]}[|endofturn|]\n[|assistant|]<thought>\n"
        prompts.append(prompt)
    
    # 출력 데이터 준비
    responses = [f"{output}\n</thought>{output}[|endofturn|]" for output in examples["output"]]
    
    # 입력과 출력 결합
    texts = [prompt + response for prompt, response in zip(prompts, responses)]
    
    # 토큰화
    encodings = tokenizer(texts, truncation=True, padding="max_length", max_length=2048)
    
    # 입력 ID 생성
    input_ids = encodings["input_ids"]
    attention_mask = encodings["attention_mask"]
    
    # 레이블 설정 (입력 ID와 동일하게 설정)
    labels = input_ids.copy()
    
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels
    }

# 데이터셋 전처리
tokenized_dataset = dataset.map(
    preprocess_function,
    batched=True,
    remove_columns=dataset.column_names
)

# 5. 학습 설정
output_dir = "./exaone-deep-finetune"
training_args = TrainingArguments(
    output_dir=output_dir,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    num_train_epochs=3,
    weight_decay=0.01,
    warmup_ratio=0.03,
    logging_steps=10,
    save_steps=100,
    fp16=True,
    report_to="none",
)

# 6. 데이터 콜레이터 설정
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# 7. 트레이너 설정 및 학습
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=data_collator,
)

# 학습 시작
trainer.train()

# 8. 모델 저장 (수정된 부분)
final_model_dir = "./exaone-deep-finetune-final"

# LoRA 어댑터와 기본 모델 병합
print("LoRA 어댑터와 기본 모델 병합 중...")
merged_model = model.merge_and_unload()  # LoRA 가중치를 기본 모델에 병합

# 병합된 전체 모델 저장
merged_model.save_pretrained(final_model_dir)
tokenizer.save_pretrained(final_model_dir)


# HF 모델을 GGUF로 변환
subprocess.run(f"python llama.cpp/convert_hf_to_gguf.py {final_model_dir} --outfile {final_model_dir}/model.gguf --outtype f16", shell=True)

# 양자화 옵션 (선택적)
print("모델 양자화 중...")
quantization_types = ["q4_k_m"]  # 다양한 양자화 옵션

for quant_type in quantization_types:
    output_file = f"{final_model_dir}/model-{quant_type}.gguf"
    subprocess.run(f"cd llama.cpp && ./quantize ../{final_model_dir}/model.gguf ../{output_file} {quant_type.upper()}", shell=True)
    print(f"{quant_type} 양자화 완료: {output_file}")

print("GGUF 변환 및 양자화 완료!")

# # 9. 모델을 GGUF 형식으로 변환
# print("모델을 GGUF 형식으로 변환 중...")

# # 먼저 F16 GGUF 형식으로 변환
# llama_cpp_dir = "./llama.cpp"  # llama.cpp 디렉토리 경로
# convert_script = os.path.join(llama_cpp_dir, "convert_hf_to_gguf.py")

# gguf_output_dir = "./gguf_models"
# os.makedirs(gguf_output_dir, exist_ok=True)
# f16_gguf_path = os.path.join(gguf_output_dir, "exaone-deep-finetune-f16.gguf")

# # 원본 모델의 config.json 가져오기
# config = AutoConfig.from_pretrained(
#     model_name,
#     trust_remote_code=True,
# )

# # 파인튜닝된 모델 디렉토리에 config.json 저장
# output_dir = "./exaone-deep-finetune-final"
# os.makedirs(output_dir, exist_ok=True)
# config.to_json_file(os.path.join(output_dir, "config.json"))

# convert_cmd = [
#     "python", convert_script,
#     final_model_dir,
#     "--outfile", f16_gguf_path,
#     "--outtype", "f16"
# ]

# print("F16 GGUF 변환 명령어:", " ".join(convert_cmd))
# subprocess.run(convert_cmd, check=True)
# print(f"F16 GGUF 변환 완료: {f16_gguf_path}")

# # 10. Q4 양자화 수행
# print("Q4 양자화 수행 중...")
# q4_gguf_path = os.path.join(gguf_output_dir, "exaone-deep-finetune-q4_k_m.gguf")
# quantize_path = os.path.join(llama_cpp_dir, "quantize")

# # 양자화 수행 (Q4_K_M 형식 사용)
# quantize_cmd = [
#     quantize_path,
#     f16_gguf_path,
#     q4_gguf_path,
#     "Q4_K_M"
# ]

# print("Q4 양자화 명령어:", " ".join(quantize_cmd))
# subprocess.run(quantize_cmd, check=True)
# print(f"Q4 양자화 완료: {q4_gguf_path}")

# print("모든 과정이 완료되었습니다.")
# print(f"파인튜닝된 모델: {final_model_dir}")
# print(f"F16 GGUF 모델: {f16_gguf_path}")
# print(f"Q4 GGUF 모델: {q4_gguf_path}")
