import os, sys, random
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unsloth import FastLanguageModel
from unsloth.chat_templates import get_chat_template
from trl import SFTTrainer, SFTConfig
from transformers import TrainingArguments, DataCollatorForSeq2Seq
from datasets import Dataset
from Grammar.grammar_ver1_1_4 import grammar
import torch, yaml, re, subprocess

max_seq_length = 4096 # Choose any! We auto support RoPE Scaling internally!
dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
load_in_4bit = True # Use 4bit quantization to reduce memory usage. Can be False.

# 4bit pre quantized models we support for 4x faster downloading + no OOMs.
fourbit_models = [
    "unsloth/Qwen2.5-Coder-7B-bnb-4bit",
    "unsloth/codellama-7b-bnb-4bit",
    "unsloth/gemma-3-12b-it-unsloth-bnb-4bit",
    "unsloth/codegemma-7b-bnb-4bit",
] # More models at https://huggingface.co/unsloth

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen2.5-Coder-7B-bnb-4bit",
    # model_name = "unsloth/qwen2.5-coder-3b-instruct-bnb-4bit",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
    # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)

model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)

tokenizer = get_chat_template(
    tokenizer,
    chat_template = "qwen-2.5",
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
        file_name = f"../Testset/TestsetWithDevices_translated/category_{i}.yaml"
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
            for item in data:
                result = read_yaml(item)
                devices = result['devices']
                # 7개 이상의 장치가 없으면 무작위로 추가
                if len(devices) < 7:
                    devices = list(set(devices + random.sample(classes.keys(), 7 - len(devices))))
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
                            "content": f"Current Time: {current_time}\n\nGenerate JOI Lang code for \"{result['command']}\"",
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

print(f"커스텀 데이터셋 크기: {len(MY_DATASET)}")
print("샘플 데이터:")
print(MY_DATASET[0]['text'][:500] + "..." if len(MY_DATASET) > 0 else "데이터 없음")

######################################################################################


trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = MY_DATASET,
    packing = True,  # Can make training 5x faster for short sequences.
    args = SFTConfig(
        per_device_train_batch_size = 4,
        gradient_accumulation_steps = 2,
        warmup_steps = 5,
        num_train_epochs = 2,
        # max_steps = 20,
        learning_rate = 2e-4,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        dataset_text_field = "text",
        report_to = "none",  # Use this for WandB etc
        max_grad_norm = 0.3,
        dataset_num_proc = 4,
        dataloader_num_workers = 4,
        logging_steps=50,
    ),
)

trainer_stats = trainer.train()

model.save_pretrained_gguf("model", tokenizer, quantization_method = "q4_k_m")