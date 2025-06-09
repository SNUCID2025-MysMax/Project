# import os, sys, random
from datetime import datetime
import re

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

model_name = "qwenCoder"

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=f"./models/{model_name}-model",
    max_seq_length=4096,
    dtype=None,
    load_in_4bit=True,
)

# ./model에서 어댑터 로드
model.load_adapter(f"./models/{model_name}-adapter")

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


with open("./ServiceExtraction/integration/service_list_ver1.1.8.txt", "r") as f:
    service_doc = f.read()
classes = extract_classes_by_name(service_doc)

FastLanguageModel.for_inference(model) # Enable native 2x faster inference

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
command = "Turn on the air conditioner"
# command = "Set the air conditioner mode to cool"
messages = [
    {"role": "system", "content": grammar},
    {"role": "system", "content": classes["AirConditioner"]},
    {"role": "user", "content": f"Current Time: {current_time}\n\nGenerate JOI Lang code for \"{command}\""},
]

from unsloth.chat_templates import get_chat_template
stop_token_ids = []
if model_name == "codegemma":
    tokenizer = get_chat_template(
        tokenizer,
        chat_template = "chatml",
        map_eos_token = True,
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
elif model_name == "gemma3":

    messages = [
        {
            "role": "system",
            "content": [{
                "type": "text", 
                "text": grammar + "\n\n" + classes["AirConditioner"]
            }]
        },
        {
            "role": "user",
            "content": [{
                "type": "text",
                "text": f"Current Time: {current_time}\n\nGenerate JOI Lang code for \"{command}\""
            }]
        }
    ]

    tokenizer = get_chat_template(
        tokenizer,
        chat_template = "gemma-3",
    )

    tokenizer.add_bos_token = False

    stop_tokens = [
        "<end_of_turn>"
    ]
    stop_token_ids = [tokenizer.tokenizer.convert_tokens_to_ids(token) for token in stop_tokens if token in tokenizer.tokenizer.get_vocab()]

elif model_name == "qwenCoder":
    # tokenizer = get_chat_template(
    #     tokenizer,
    #     chat_template = "qwen-2.5",
    # )
    tokenizer = get_chat_template(
        tokenizer,
        chat_template = "chatml",
        map_eos_token = True,
    )

    tokenizer.add_bos_token = False


    stop_tokens = [
            "<|im_end|>", "<|endoftext|>", "<|file_sep|>", "<|fim_prefix|>", "<|fim_middle|>",
            "<|fim_suffix|>", "<|fim_pad|>", "<|repo_name|>", "<|im_start|>",
            "<|object_ref_start|>", "<|object_ref_end|>", "<|box_start|>", "<|box_end|>",
            "<|quad_start|>", "<|quad_end|>", "<|vision_start|>", "<|vision_end|>",
            "<|vision_pad|>", "<|image_pad|>", "<|video_pad|>"
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
# outputs = model.generate(
#     input_ids = inputs, 
#     eos_token_id=stop_token_ids,
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