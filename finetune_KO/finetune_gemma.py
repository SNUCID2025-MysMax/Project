from unsloth import FastModel
from unsloth.chat_templates import get_chat_template
from trl import SFTTrainer, SFTConfig
from datasets import Dataset
from Grammar.grammar_ver1_1_4 import grammar
import torch, yaml, re

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
    model_name = "unsloth/gemma-3-12b-it-unsloth-bnb-4bit",
    max_seq_length = 8192, # Choose any for long context!
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

    r = 16,           # Larger = higher accuracy, but might overfit
    lora_alpha = 16,  # Recommended alpha == r at least
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
                            "content": f"Generate SoP Lang code for \"{result['command']}\"",
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
    eval_dataset = None, # Can set up evaluation!
    args = SFTConfig(
        dataset_text_field = "text",
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4, # Use GA to mimic batch size!
        warmup_steps = 5,
        num_train_epochs = 5, # Set this for 1 full training run.
        # max_steps = 30,
        learning_rate = 1e-4, # Reduce to 2e-5 for long training runs
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        report_to = "none", # Use this for WandB etc
        dataset_num_proc=2,
    ),
)
trainer_stats = trainer.train()

model.save_pretrained_gguf("model", tokenizer, quantization_method = "q4_k_m")