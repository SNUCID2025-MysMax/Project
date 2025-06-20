import multiprocessing
import os, sys, random, copy, json
from tqdm import tqdm
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unsloth import FastLanguageModel, is_bfloat16_supported
from unsloth.chat_templates import get_chat_template
from trl import SFTTrainer, SFTConfig
from datasets import Dataset
from Grammar.grammar_ver1_1_10 import grammar
import torch, yaml, re
from torch.nn.attention import SDPBackend, sdpa_kernel

max_seq_length = 4096
# max_seq_length = 3072
dtype = (
    None  # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
)
load_in_4bit = True  # Use 4bit quantization to reduce memory usage. Can be False.

# 4bit pre quantized models we support for 4x faster downloading + no OOMs.
fourbit_models = [
    "unsloth/Qwen2.5-Coder-7B-bnb-4bit",
    "unsloth/codellama-7b-bnb-4bit",
    "unsloth/gemma-3-12b-it-unsloth-bnb-4bit",
    "unsloth/codegemma-7b-bnb-4bit",
] # More models at https://huggingface.co/unsloth

model_name = "unsloth/Qwen2.5-Coder-7B-Instruct-bnb-4bit" 

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = model_name,  # Choose ANY! eg teknium/OpenHermes-2.5-Mistral-7B
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
    # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)

model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj"],
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
    chat_template = "chatml",
    map_eos_token=True,
)

tokenizer.add_bos_token = False

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

with open("../ServiceExtraction/integration/service_list_ver1.1.9.txt", "r") as f:
    service_doc = f.read()
classes = extract_classes_by_name(service_doc)
classes_copy = copy.deepcopy(classes)

extra_tags = ["Upper", "Lower", "SectorA", "SectorB", "Wall", "Odd", "Even"]
def read_yaml(data):
    dic = {}
    dic['command'] = data['command_translated']
    dic['devices'] = data['devices']

    code = data['code'][0]
    has_break = 'Y' if 'break' in code else 'N'
    has_all = 'Y' if 'all(' in code or 'All(' in code else 'N'
    has_any = 'Y' if 'any(' in code or 'Any(' in code else 'N'
    k = f"""cron = \"{data['cron']}\", period = {data['period']}, break = {has_break}
    all = {has_all}, any = {has_any}
    ```joi
    {code['code'].strip()}
    ```
    """
    dic["code"] = k
    return dic

def read_yaml2(data):
    dic = {}
    dic['command'] = data['command']

    result = set()
    for code in data["code"]:
        text = code["code"]
        matches = re.findall(r"#([A-Za-z0-9]+)(?=[^A-Za-z0-9])", text)
        matches = {m for m in matches if m not in extra_tags}
        result.update(matches)
    dic['devices'] = list(result)

    code = data['code'][0]
    has_break = 'Y' if 'break' in code else 'N'
    has_all = 'Y' if 'all(' in code or 'All(' in code else 'N'
    has_any = 'Y' if 'any(' in code or 'Any(' in code else 'N'
    k = f"""cron = \"{data['cron']}\", period = {data['period']}, break = {has_break}
    all = {has_all}, any = {has_any}
    ```joi
    {code['code'].strip()}
    ```
    """
    dic["code"] = k
    return dic

# 데이터셋 생성 부분 수정
def load_dataset():
    global classes
    extra_tags = ["Upper", "Lower", "SectorA", "SectorB", "Wall", "Odd", "Even"]
    ret = []
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    lst = list(range(0, 12)) + [13]
    for i in lst:  # 범위를 필요에 따라 조정
        if (i == 13 or i == 15):
            for key in classes.keys():
                doc = classes[key]
                lines = doc.splitlines()
                new_lines = lines[:4] + [f"    #{tag}" for tag in sorted(set(extra_tags))] + lines[4:]
                classes[key] = "\n".join(new_lines)
        
        file_name = f"../Testset/TestsetWithDevices_translated/category_{i}.yaml"
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
            for idx, item in enumerate(data):
                if idx < 5:
                    continue
                result = read_yaml(item)
                devices = result['devices']
                service_doc = "\n---\n".join([classes[device] for device in devices if device in classes])
                ret.append({
                    "conversations": [
                        {
                            "role": "system",
                            "content": f"{grammar}\n<DEVICES>\n{service_doc}\n</DEVICES>",
                        },
                        {
                            "role": "user",
                            "content": f"Current Time: {current_time}\n\nGenerate JOI Lang code for: \"{result['command']}\"",
                            # "content": f"Generate JOI Lang code for \"{result['command']}\"",
                        },
                        {
                            "role": "assistant",
                            "content": result['code'].strip() + "\n",
                        }
                    ]
                })
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {file_name}")
        except Exception as e:
            print(f"데이터 처리 중 오류: {e}")

        file_name = f"../ChatGPT/data_augment/trainset_yaml_parameter/generated_data_{i}.yaml"
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                # data = json.load(file)
                data = yaml.safe_load(file)
            for item in data:
                result = read_yaml2(item)
                devices = result['devices']
                service_doc = "\n---\n".join([classes[device] for device in devices if device in classes])
                ret.append({
                    "conversations": [
                        {
                            "role": "system",
                            "content": f"{grammar}\n<DEVICES>\n{service_doc}\n</DEVICES>",
                        },
                        {
                            "role": "user",
                            "content": f"Current Time: {current_time}\n\nGenerate JOI Lang code for \"{result['command']}\"",
                        },
                        {
                            "role": "assistant",
                            "content": result['code'].strip() + "\n",
                        }
                    ]
                })
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {file_name}")
        except Exception as e:
            print(f"데이터 처리 중 오류: {e}")

        if (i == 13 or i == 15):
            classes = classes_copy     
    
    return ret

# 커스텀 데이터셋 생성
data_set = load_dataset()
MY_DATASET = Dataset.from_list(data_set)

# 포매팅 적용
MY_DATASET = MY_DATASET.map(
    formatting_prompts_func,
    batched=True,
    remove_columns=["conversations"],
)

# dataset_split = MY_DATASET.train_test_split(test_size=0.15, seed=3407)
# train_dataset = dataset_split['train']
# eval_dataset = dataset_split['test']

# print(f"커스텀 데이터셋 크기: {len(MY_DATASET)}")
# # print(MY_DATASET[0]['text'])
sample_text = MY_DATASET[0]['text']
tokens = tokenizer.encode(sample_text)
decoded = tokenizer.decode(tokens)
# # print("Original:", sample_text)
# print("Decoded:", decoded)

# 토큰 길이 측정
lengths = []
for example in tqdm(MY_DATASET):
    text = example["text"]  # formatting_prompts_func 결과가 "text" 필드에 들어갔다면
    tokens = tokenizer.encode(text, truncation=False)
    lengths.append(len(tokens))

# 통계 출력
print(f"Total samples: {len(lengths)}")
print(f"Max length: {max(lengths)}")
print(f"Min length: {min(lengths)}")
print(f"Average length: {sum(lengths) / len(lengths):.2f}")
######################################################################################

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = MY_DATASET,
    packing = False, 
    args = SFTConfig(
        use_liger_kernel = True,
        per_device_train_batch_size = 4,
        gradient_accumulation_steps = 4,
        max_seq_length = max_seq_length,
        # warmup_steps = 10,
        warmup_ratio = 0.05,
        num_train_epochs = 1.5,
        learning_rate = 2e-5, #1e-6
        optim = "adamw_8bit",
        weight_decay = 0.01,
        max_grad_norm = 0.3,
        lr_scheduler_type = "cosine",
        seed = 3407,
        dataset_text_field = "text",
        report_to = "none",
        dataset_num_proc = min(8, multiprocessing.cpu_count()),
        dataloader_num_workers = min(8, multiprocessing.cpu_count()),
        logging_steps= 15,
        # auto_find_batch_size = True,
        fp16 = False,
        bf16 = True, 
        remove_unused_columns = True,
        dataloader_pin_memory = False,
    ),
)

with sdpa_kernel(SDPBackend.FLASH_ATTENTION):
    trainer_stats = trainer.train()


model.save_pretrained("../models/qwenCoder-adapter")
tokenizer.save_pretrained("../models/qwenCoder-adapter")

# 파인튜닝 정보 저장
import os
import json

# 저장 경로 생성
save_dir = "../models/qwenCoder-adapter"
os.makedirs(save_dir, exist_ok=True)
json_path = os.path.join(save_dir, "training_info.json")

# LoRA 설정 추출
peft_filter = ["base_model_name_or_path", "r", "lora_alpha", "lora_dropout", "target_modules"]
peft_info = {}

for adapter_name, config in model.peft_config.items():
    peft_info[adapter_name] = {
        k: list(getattr(config, k)) if isinstance(getattr(config, k), (set, tuple)) else getattr(config, k)
        for k in peft_filter if hasattr(config, k)
    }

# Tokenizer 설정 추출
tokenizer_info = {
    "add_bos_token": tokenizer.add_bos_token,
    "chat_template": getattr(tokenizer, "chat_template", "chatml (set manually)"),
    "vocab_size": tokenizer.vocab_size,
    "special_tokens_map": tokenizer.special_tokens_map,
}

# Trainer 설정 추출
trainer_filter = [
    "per_device_train_batch_size", "gradient_accumulation_steps",
    "warmup_steps", "num_train_epochs", "learning_rate", "weight_decay",
    "max_grad_norm", "lr_scheduler_type", "bf16", "fp16",
    "dataloader_num_workers", "dataset_num_proc", "remove_unused_columns", "optim"
]

# 필터링 + max_seq_length 직접 포함
trainer_info = {
    k: trainer.args.to_dict()[k] for k in trainer_filter if k in trainer.args.to_dict()
}

# 전체 정보 구조화
training_info = {
    "model_name": model_name,
    "max_seq_length": max_seq_length,
    "lora_config": peft_info,
    "tokenizer_config": tokenizer_info,
    "trainer_config": trainer_info,
}

# JSON 저장
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(training_info, f, indent=2, ensure_ascii=False)

print(f"🔧 Training info saved to {json_path}")
