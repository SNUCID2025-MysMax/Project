import multiprocessing
import os, sys, random
from tqdm import tqdm
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unsloth import FastLanguageModel, is_bfloat16_supported
from unsloth.chat_templates import get_chat_template
from trl import SFTTrainer, SFTConfig
from datasets import Dataset
from Grammar.grammar_ver1_1_5 import grammar
import torch, yaml, re
from torch.nn.attention import SDPBackend, sdpa_kernel

max_seq_length = 3072  # Gemma sadly only supports max 8192 for now
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

model_name = "unsloth/gemma-3-4b-it-unsloth-bnb-4bit"

# from transformers import AutoTokenizer
# original_tokenizer = AutoTokenizer.from_pretrained(model_name)
# original_tokenizer.save_pretrained("model")

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = model_name,  # Choose ANY! eg teknium/OpenHermes-2.5-Mistral-7B
    max_seq_length = max_seq_length,
    load_in_4bit = load_in_4bit,
    full_finetuning = False,
    # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)

model = FastLanguageModel.get_peft_model(
    model,
    finetune_vision_layers     = False, # Turn off for just text!
    finetune_language_layers   = True,  # Should leave on!
    finetune_attention_modules = True,  # Attention good for GRPO
    finetune_mlp_modules       = True,  # SHould leave on always!

    r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    # target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
    #                   "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 32,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    random_state = 3407,
)


tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-3",
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

with open("../ServiceExtraction/integration/service_list_ver1.1.8.txt", "r") as f:
    service_doc = f.read()
classes = extract_classes_by_name(service_doc)

def read_yaml(data):
    dic = {}
    dic['command'] = data['command_translated']
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

    for i in range(0, 17):  # 범위를 필요에 따라 조정
        file_name = f"../Testset/TestsetWithDevices_translated/category_{i}.yaml"
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
            for item in data:
                result = read_yaml(item)
                devices = result['devices']
                # # 7개 이상의 장치가 없으면 무작위로 추가
                # if len(devices) < 7:
                #     devices = list(set(devices + random.sample(list(classes.keys()), 7 - len(devices))))
                service_doc = "\n---\n".join([classes[device] for device in devices if device in classes])
                ret.append({
                    "conversations": [
                        # {
                        #     "role": "system",
                        #     "content": grammar,
                        # },
                        {
                            "role": "system", 
                            # "content": grammar + "\n\n" + service_doc,
                            "content": service_doc,
                        },
                        {
                            "role": "user",
                            # "content": f"Current Time: {current_time}\n\nGenerate JOI Lang code for \"{result['command']}\"",
                            "content": f"Generate JOI Lang code for \"{result['command']}\"",
                        },
                        {
                            "role": "assistant",
                            "content": "```\n"+result['code']+"\n```",
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
    # batch_size=32,
    # remove_columns=["conversations"]
)

print(f"커스텀 데이터셋 크기: {len(MY_DATASET)}")
# print("샘플 데이터:")
# print(MY_DATASET[0]['text'][:500] + "..." if len(MY_DATASET) > 0 else "데이터 없음")

print(MY_DATASET[0]['text'])
sample_text = MY_DATASET[0]['text']
tokens = tokenizer.tokenizer.encode(sample_text)
decoded = tokenizer.tokenizer.decode(tokens)
print("Original:", sample_text)
print("Decoded:", decoded)

# 토큰 길이 측정
lengths = []
for example in tqdm(MY_DATASET):
    text = example["text"]  # formatting_prompts_func 결과가 "text" 필드에 들어갔다면
    tokens = tokenizer.tokenizer.encode(text, truncation=False)
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
    packing = False,  # Can make training 5x faster for short sequences.
    args = SFTConfig(
        use_liger_kernel = False,
        per_device_train_batch_size = 4,
        gradient_accumulation_steps = 4,
        warmup_steps = 0,
        num_train_epochs = 2,
        # max_steps = 200,
        learning_rate = 5e-6, #1e-6
        optim = "adamw_8bit",
        weight_decay = 0.02,
        lr_scheduler_type = "constant",
        seed = 3407,
        dataset_text_field = "text",
        report_to = "none",  # Use this for WandB etc
        max_grad_norm = 0.2,
        dataset_num_proc = min(8, multiprocessing.cpu_count()),
        dataloader_num_workers = min(8, multiprocessing.cpu_count()),
        logging_steps= 10,
        auto_find_batch_size = True,
        fp16 = False,
        bf16 = True, 
    ),
)

# with sdpa_kernel(SDPBackend.FLASH_ATTENTION):
#     trainer_stats = trainer.train()

trainer_stats = trainer.train()

# # import gc
# # torch.cuda.empty_cache()
# # gc.collect()

model.save_pretrained("../models/gemma3-adapter")
tokenizer.save_pretrained("../models/gemma3-adapter")

# # model.save_pretrained_merged("model", tokenizer, save_method="merged_16bit")
# # model.save_pretrained_gguf("model", tokenizer, quantization_method = "q4_k_m")