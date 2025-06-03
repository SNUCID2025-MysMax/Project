# import os, sys, random
from datetime import datetime
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

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "model",
    max_seq_length = 4096,
    dtype = None,
    load_in_4bit = True,
)

FastLanguageModel.for_inference(model) # Enable native 2x faster inference

current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
messages = [
    {"from": "human", "value": grammar},
    {"from": "human", "value": f"Current Time: {current_time}\n\nGenerate JOI Lang code for \"Turn on the air conditioner.\""},
]

from unsloth.chat_templates import get_chat_template
tokenizer = get_chat_template(
    tokenizer,
    chat_template = "chatml", # Supports zephyr, chatml, mistral, llama, alpaca, vicuna, vicuna_old, unsloth
    mapping = {"role" : "from", "content" : "value", "user" : "human", "assistant" : "gpt", "system": "system"}, # ShareGPT style
    map_eos_token = False, # Maps <|im_end|> to </s> instead
)

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize = True,
    add_generation_prompt = True, # Must add for generation
    return_tensors = "pt",
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer)
_ = model.generate(
    input_ids = inputs, 
    eos_token_id=tokenizer.convert_tokens_to_ids("<|im_end|>"),
    pad_token_id=tokenizer.pad_token_id,
    streamer = text_streamer, 
    max_new_tokens = 128, use_cache = True)