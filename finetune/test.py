# import os, sys, random
from datetime import datetime
import re
# from unsloth import FastLanguageModel
# from unsloth.chat_templates import get_chat_template

# max_seq_length = 4096  # Gemma sadly only supports max 8192 for now
# dtype = (
#     None  # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
# )
# load_in_4bit = True  # Use 4bit quantization to reduce memory usage. Can be False.

# # 4bit pre quantized models we support for 4x faster downloading + no OOMs.
# fourbit_models = [
#     "unsloth/Qwen2.5-Coder-7B-bnb-4bit",
#     "unsloth/codellama-7b-bnb-4bit",
#     "unsloth/gemma-3-12b-it-unsloth-bnb-4bit",
#     "unsloth/codegemma-7b-bnb-4bit",
# ] # More models at https://huggingface.co/unsloth

# model_name = "unsloth/codegemma-7b-bnb-4bit" 

from unsloth import FastLanguageModel
from unsloth.chat_templates import get_chat_template
from transformers import AutoTokenizer
from peft import PeftModel
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Grammar.grammar_ver1_1_5 import grammar

# model, tokenizer = FastLanguageModel.from_pretrained(
#     model_name = "model",
#     max_seq_length = 4096,
#     dtype = None,
#     load_in_4bit = True,
# )

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="./codegemma",
    max_seq_length=4096,
    dtype=None,
    load_in_4bit=True,
)

# ./model에서 어댑터 로드
model.load_adapter("./model")

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

FastLanguageModel.for_inference(model) # Enable native 2x faster inference

current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
messages = [
    {"role": "system", "content": grammar},
    {"role": "system", "content": classes["AirConditioner"]},
    {"role": "user", "content": f"Current Time: {current_time}\n\nGenerate JOI Lang code for \"Set the air conditioner mode to cool\""},
]

from unsloth.chat_templates import get_chat_template
tokenizer = get_chat_template(
    tokenizer,
    chat_template = "chatml", # Supports zephyr, chatml, mistral, llama, alpaca, vicuna, vicuna_old, unsloth
    # mapping = {"role" : "from", "content" : "value", "user" : "human", "assistant" : "gpt", "system": "system"}, # ShareGPT style
    map_eos_token = True, # Maps <|im_end|> to </s> instead
)

tokenizer.add_bos_token = False

stop_tokens = [
    "<|im_end|>",
    "<|file_separator|>", 
    "<|fim_prefix|>",
    "<|fim_middle|>",
    "<|fim_suffix|>"
]

stop_token_ids = [tokenizer.convert_tokens_to_ids(token) for token in stop_tokens if token in tokenizer.get_vocab()]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize = True,
    add_generation_prompt = True, # Must add for generation
    return_tensors = "pt",
).to("cuda")

# from transformers import TextStreamer
# text_streamer = TextStreamer(tokenizer)
# _ = model.generate(
#     input_ids = inputs, 
#     eos_token_id=stop_token_ids,  # 여러 stop 토큰 설정
#     pad_token_id=tokenizer.pad_token_id,
#     streamer = text_streamer, 
#     max_new_tokens = 128, use_cache = True)

outputs = model.generate(
    input_ids=inputs, 
    eos_token_id=stop_token_ids,
    pad_token_id=tokenizer.pad_token_id,
    max_new_tokens=128, 
    use_cache=True
)

generated_ids = outputs[0][len(inputs[0]):]
last_token_id = generated_ids[-1].item()

if last_token_id in stop_token_ids:
    generated_ids = generated_ids[:-1]  # 마지막 토큰 제거

response_text = tokenizer.decode(generated_ids, skip_special_tokens=True)
print(response_text.strip())