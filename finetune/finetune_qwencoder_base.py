import multiprocessing
import os, sys, random, copy, json
from tqdm import tqdm
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unsloth import FastLanguageModel, is_bfloat16_supported
from unsloth.chat_templates import get_chat_template
from trl import SFTTrainer, SFTConfig
from datasets import Dataset
from Grammar.grammar_ver1_1_6 import grammar
import torch, yaml, re
from torch.nn.attention import SDPBackend, sdpa_kernel

max_seq_length = 4096  # Gemma sadly only supports max 8192 for now
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

model_name = "unsloth/Qwen2.5-Coder-7B-bnb-4bit" 

# from transformers import AutoTokenizer
# original_tokenizer = AutoTokenizer.from_pretrained(model_name)
# original_tokenizer.save_pretrained("model")

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = model_name,  # Choose ANY! eg teknium/OpenHermes-2.5-Mistral-7B
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
    # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)

model = FastLanguageModel.get_peft_model(
    model,
    r = 32, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 32,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = True,  # We support rank stabilized LoRA
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

with open("../ServiceExtraction/integration/service_list_ver1.1.8.txt", "r") as f:
    service_doc = f.read()
classes = extract_classes_by_name(service_doc)

classes_copy = copy.deepcopy(classes)

exclude = {"Wall", "SectorA", "SectorB", "Upper", "Lower", "Even", "Odd"}
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

def read_json(data):
    dic = {}
    dic['command'] = data['command_translated']

    result = set()
    for code in data["code"]:
        text = code["code"]
        matches = re.findall(r"#([A-Za-z0-9]+)(?=[^A-Za-z0-9])", text)
        matches = {m for m in matches if m not in exclude}
        result.update(matches)
    dic['devices'] = list(result)

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
    global classes
    ret = []
    current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")

    extra_tags = ["Upper", "Lower", "SectorA", "SectorB", "Wall", "Odd", "Even",]

    for i in range(0, 17):  # 범위를 필요에 따라 조정
        
        if (i == 13):
            for key in classes.keys():
                doc = classes[key]
                lines = doc.splitlines()
                new_lines = lines[:4] + [f"    #{tag}" for tag in sorted(set(extra_tags))] + lines[4:]
                classes[key] = "\n".join(new_lines)

        # file_name = f"../Testset/TestsetWithDevices_translated/category_{i}.yaml"
        # try:
        #     with open(file_name, "r", encoding="utf-8") as file:
        #         data = yaml.safe_load(file)
        #     for item in data:
        #         result = read_yaml(item)
        #         devices = result['devices']
        #         service_doc = "\n---\n".join([classes[device] for device in devices if device in classes])
        #         ret.append({
        #             "conversations": [
        #                 {
        #                     "role": "system",
        #                     "content": grammar,
        #                 },
        #                 {
        #                     "role": "system", 
        #                     # "content": grammar + "\n\n" + service_doc,
        #                     "content": service_doc,
        #                 },
        #                 {
        #                     "role": "user",
        #                     "content": f"Current Time: {current_time}\n\nGenerate JOI Lang code for \"{result['command']}\"",
        #                     # "content": f"Generate JOI Lang code for \"{result['command']}\"",
        #                 },
        #                 {
        #                     "role": "assistant",
        #                     "content": "```\n"+result['code']+"\n```",
        #                 }
        #             ]
        #         })
        # except FileNotFoundError:
        #     print(f"파일을 찾을 수 없습니다: {file_name}")
        # except Exception as e:
        #     print(f"데이터 처리 중 오류: {e}") 
        
        file_name = f"../ChatGPT/data_augmenta/trainset/generated_data_{i}.json"
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
            for item in data:
                result = read_json(item)
                devices = result['devices']
                service_doc = "\n---\n".join([classes[device] for device in devices if device in classes])
                ret.append({
                    "conversations": [
                        {
                            "role": "system",
                            "content": grammar,
                        },
                        {
                            "role": "system", 
                            # "content": grammar + "\n\n" + service_doc,
                            "content": service_doc,
                        },
                        {
                            "role": "user",
                            "content": f"Current Time: {current_time}\n\nGenerate JOI Lang code for \"{result['command']}\"",
                            # "content": f"Generate JOI Lang code for \"{result['command']}\"",
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


        if (i == 13):
            classes = classes_copy 
    
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
tokens = tokenizer.encode(sample_text)
decoded = tokenizer.decode(tokens)
print("Original:", sample_text)
print("Decoded:", decoded)

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

# trainer = SFTTrainer(
#     model = model,
#     tokenizer = tokenizer,
#     train_dataset = MY_DATASET,
#     packing = False,  # Can make training 5x faster for short sequences.
#     args = SFTConfig(
#         use_liger_kernel = True,
#         per_device_train_batch_size = 4,
#         gradient_accumulation_steps = 4,
#         warmup_steps = 10,
#         num_train_epochs = 3,
#         learning_rate = 2e-5, #1e-6
#         optim = "adamw_8bit",
#         weight_decay = 0.01,
#         lr_scheduler_type = "cosine",
#         seed = 3407,
#         dataset_text_field = "text",
#         report_to = "none",
#         max_grad_norm = 0.3,
#         dataset_num_proc = min(8, multiprocessing.cpu_count()),
#         dataloader_num_workers = min(4, multiprocessing.cpu_count()),
#         logging_steps= 5,
#         auto_find_batch_size = True,
#         fp16 = False,
#         bf16 = True, 
#         remove_unused_columns = False,
#         dataloader_pin_memory = False,
#     ),
# )

# with sdpa_kernel(SDPBackend.FLASH_ATTENTION):
#     trainer_stats = trainer.train()

# # trainer_stats = trainer.train()

# # # import gc
# # # torch.cuda.empty_cache()
# # # gc.collect()

# model.save_pretrained("../models/qwenCoder-adapter")
# tokenizer.save_pretrained("../models/qwenCoder-adapter")

# # # model.save_pretrained_merged("model", tokenizer, save_method="merged_16bit")
# # # model.save_pretrained_gguf("model", tokenizer, quantization_method = "q4_k_m")