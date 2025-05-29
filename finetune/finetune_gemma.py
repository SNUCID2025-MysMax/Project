import os, sys, gc
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unsloth import FastModel
from unsloth.chat_templates import get_chat_template
from trl import SFTTrainer, SFTConfig
from datasets import Dataset
from Grammar.grammar_ver1_1_4 import grammar
import torch, yaml, re


# def clear_memory():
#     gc.collect()
#     if torch.cuda.is_available():
#         torch.cuda.empty_cache()
#         torch.cuda.synchronize()

# 4bit pre quantized models we support for 4x faster downloading + no OOMs.
fourbit_models = [
    "unsloth/mistral-7b-bnb-4bit",
    "unsloth/mistral-7b-instruct-v0.2-bnb-4bit",
    "unsloth/llama-2-7b-bnb-4bit",
    "unsloth/llama-2-13b-bnb-4bit",
    "unsloth/codellama-34b-bnb-4bit",
    "unsloth/tinyllama-bnb-4bit",
    "unsloth/gemma-7b-bnb-4bit",  # New Google 6 trillion tokens model 2.5x faster!
    "unsloth/gemma-2b-bnb-4bit",
]  # More models at https://huggingface.co/unsloth

model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/gemma-3-4b-it-unsloth-bnb-4bit",
    max_seq_length = 4096, # Choose any for long context!
    load_in_4bit = True,  # 4 bit quantization to reduce memory
    load_in_8bit = False, # [NEW!] A bit more accurate, uses 2x memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
    # token = "hf_...", # use one if using gated models
)

model = FastModel.get_peft_model(
    model,
    finetune_vision_layers     = False, # Turn off for just text!
    finetune_language_layers   = True,  # Should leave on!
    finetune_attention_modules = True,  # Attention good for GRPO
    finetune_mlp_modules       = True,  # SHould leave on always!

    r = 8,           # Larger = higher accuracy, but might overfit
    lora_alpha = 8,  # Recommended alpha == r at least
    lora_dropout = 0,
    bias = "none",
    random_state = 3407,
)

tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-3",
)

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

with open("../ServiceExtraction/integration/service_list_ver1.1.7.txt", "r") as f:
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
    current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
    for i in range(0, 16):  # 범위를 필요에 따라 조정
        file_name = f"../Testset/TestsetWithDevices/category_{i}.yaml"
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
                            "content": grammar + "\n\n" + service_doc
                        },
                        # {
                        #     "role": "system",
                        #     "content": service_doc
                        # },
                        {
                            "role": "user",
                            "content": f"Current Time: {current_time}\n\nGenerate SoP Lang code for \"{result['command']}\""
                        },
                        {
                            "role": "assistant",
                            "content": result['code']
                        }
                    ]
                })
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {file_name}")
        except Exception as e:
            print(f"데이터 처리 중 오류: {e}")
    
    return ret

def load_dataset_one():
    ret = []
    current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
    
    # 첫 번째 카테고리에서 첫 번째 항목만 사용
    file_name = f"../Testset/TestsetWithDevices/category_0.yaml"
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        
        # 첫 번째 항목만 사용
        if data and len(data) > 0:
            item = data[0]  # 첫 번째 항목만
            result = read_yaml(item)
            service_doc = "\n".join([classes[device] for device in result['devices'] if device in classes])
            ret.append({
                "conversations": [
                    {
                        "role": "system",
                        "content": grammar + "\n\n" + service_doc
                    },
                    {
                        "role": "user",
                        "content": f"Current Time: {current_time}\nGenerate SoP Lang code for \"{result['command']}\""
                    },
                    {
                        "role": "assistant",
                        "content": result['code']
                    }
                ]
            })
            print(f"테스트용 데이터 로드 완료: {result['command']}")
        else:
            print("데이터가 비어있습니다.")
            
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

print(f"커스텀 데이터셋 크기: {len(MY_DATASET)}")
print("샘플 데이터:")
print(MY_DATASET[0]['text'][:500] + "..." if len(MY_DATASET) > 0 else "데이터 없음")

######################################################################################


trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = MY_DATASET,
    packing = True,
    args = SFTConfig(
        dataset_text_field = "text",
        per_device_train_batch_size = 4,
        gradient_accumulation_steps = 2, # Use GA to mimic batch size!
        warmup_steps = 5,
        num_train_epochs = 2, # Set this for 1 full training run.
        # max_steps = 30,
        learning_rate = 2e-4, # Reduce to 2e-5 for long training runs
        logging_steps = 10,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        report_to = "none", # Use this for WandB etc
        max_grad_norm = 0.3,
        dataset_num_proc = 4,
        dataloader_num_workers = 4,
    ),
)

from unsloth.chat_templates import train_on_responses_only
trainer = train_on_responses_only(
    trainer,
    instruction_part = "<start_of_turn>user\n",
    response_part = "<start_of_turn>model\n",
)

trainer_stats = trainer.train()

del trainer
torch.cuda.empty_cache()  # GPU 메모리 정리
gc.collect()  # 가비지 컬렉션 실행


model.save_pretrained("model")
tokenizer.save_pretrained("model")

torch.cuda.empty_cache()
gc.collect()

model.save_pretrained_merged("model", tokenizer)

torch.cuda.empty_cache()
gc.collect()

model.save_pretrained_gguf(
    "model",
    quantization_type = "Q8_0", # For now only Q8_0, BF16, F16 supported
)
# # # model.save_pretrained_gguf("model", tokenizer, quantization_type = "Q8_0")