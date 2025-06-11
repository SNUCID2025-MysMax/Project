import os, sys, re, gc, yaml, time, json, copy
from datetime import datetime
import concurrent.futures

from unsloth import FastLanguageModel
from unsloth.chat_templates import get_chat_template
from transformers import AutoTokenizer
from peft import PeftModel

from FlagEmbedding import BGEM3FlagModel
from Embedding.embedding import hybrid_recommend
from Grammar.grammar_ver1_1_5 import grammar
from Testset.joi_extraction_tool import parse_scenarios, extract_last_code_block
from Validation.validate import validate_tmp
from sentence_transformers import SentenceTransformer

from yaml.representer import SafeRepresenter

# from Evaluation.compare_soplang_ir import  compare_codes

TIME_OUT = 20

class LiteralString(str): pass
def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
yaml.add_representer(LiteralString, literal_str_representer)

def extract_classes_by_name(text: str):
    pattern = r'Device\s+(\w+)\s*:\s*\n\s+"""(.*?)"""'
    matches = re.finditer(pattern, text, re.DOTALL)
    return {match.group(1): match.group(0) for match in matches}

def get_stop_token_ids(model_name, tokenizer):
    stop_tokens = {
        "codegemma": [
            "<|im_end|>", "<|file_separator|>", "<|fim_prefix|>", "<|fim_middle|>", "<|fim_suffix|>"
        ],
        "gemma3": ["<end_of_turn>"],
        "qwenCoder": [
            "<|im_end|>", "<|endoftext|>", "<|file_sep|>", "<|fim_prefix|>", "<|fim_middle|>",
            "<|fim_suffix|>", "<|fim_pad|>", "<|repo_name|>", "<|im_start|>",
            "<|object_ref_start|>", "<|object_ref_end|>", "<|box_start|>", "<|box_end|>",
            "<|quad_start|>", "<|quad_end|>", "<|vision_start|>", "<|vision_end|>",
            "<|vision_pad|>", "<|image_pad|>", "<|video_pad|>"
        ]
    }.get(model_name, [])

    vocab = tokenizer.get_vocab() if hasattr(tokenizer, "get_vocab") else tokenizer.tokenizer.get_vocab()
    convert = tokenizer.convert_tokens_to_ids if hasattr(tokenizer, "convert_tokens_to_ids") else tokenizer.tokenizer.convert_tokens_to_ids
    return [convert(token) for token in stop_tokens if token in vocab]

def build_messages(model_name, grammar, service_doc, user_command, current_time):
    if model_name == "gemma3":
        return [
            {
                "role": "system",
                "content": [{"type": "text", "text": grammar + "\n\n" + service_doc}]
            },
            {
                "role": "user",
                "content": [{"type": "text", "text": f"Current Time: {current_time}\n\nGenerate JOI Lang code for \"{user_command}\""}]
            }
        ]
    else:
        return [
            {"role": "system", "content": grammar},
            {"role": "system", "content": service_doc},
            {"role": "user", "content": f"Current Time: {current_time}\nGenerate JOI Lang code for \"{user_command}\""}
        ]

def call_model(model, inputs, stop_token_ids, tokenizer):
    return model.generate(
        input_ids=inputs,
        eos_token_id=stop_token_ids,
        pad_token_id=tokenizer.pad_token_id,
        max_new_tokens=1024,
        use_cache=True,
    )

def run_test_case_unsloth(model, tokenizer, stop_token_ids, model_name, user_command_origin, user_command, classes, service_selected):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    service_doc = "\n---\n".join([classes[i] for i in service_selected])
    messages = build_messages(model_name, grammar, service_doc, user_command, current_time)

    inputs = tokenizer.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
    ).to("cuda")

    response = ""
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(call_model, model, inputs, stop_token_ids, tokenizer)
        try:
            outputs = future.result(timeout=TIME_OUT)
            generated_ids = outputs[0][len(inputs[0]):]
            # if len(generated_ids) > 0 and generated_ids[-1].item() in stop_token_ids:
            #     generated_ids = generated_ids[:-1]
            stop_indexes = [i for i, tok_id in enumerate(generated_ids) if tok_id in stop_token_ids]
            if stop_indexes:
                generated_ids = generated_ids[:stop_indexes[0]]
            response = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
        except concurrent.futures.TimeoutError:
            response = ""
    elapsed = time.time() - start
    return response, elapsed


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# def compare_all(model_name: str):
#     # 경로 설정
#     gold_path = f"./Testset/Testset"
#     pred_path = f"./Testset/Eval_{model_name}"

#     # 모든 YAML 파일 반복
#     for file in os.listdir(gold_path):
#         if not file.endswith(".yaml"):
#             continue
        
#         print(f"\n==== Comparing: {file} ====")

#         # Load gold + prediction
#         with open(os.path.join(gold_path, file), 'r', encoding='utf-8') as f1:
#             gold_data = yaml.safe_load(f1)
#         with open(os.path.join(pred_path, f"evaluation_{file}"), 'r', encoding='utf-8') as f2:
#             pred_data = yaml.safe_load(f2)
        
        
#         for ex_idx, (gold_item, pred_item) in enumerate(zip(gold_data, pred_data)):
#             gold_scenarios = gold_item["code"]
#             pred_scenarios = pred_item["generated_code"]

#             if len(gold_scenarios) != len(pred_scenarios):
#                 print(f"[Example {ex_idx+1}] ⚠️ 길이 불일치 - gold: {len(gold_scenarios)}, pred: {len(pred_scenarios)}")
#                 continue

#             for sc_idx, (g, p) in enumerate(zip(gold_scenarios, pred_scenarios)):
#                 gold = {
#                     "name": g["name"],
#                     "cron": g["cron"],
#                     "period": g["period"],
#                     "script": g["code"]
#                 }
#                 pred = {
#                     "name": p["name"],
#                     "cron": p["cron"],
#                     "period": p["period"],
#                     "script": p["code"]
#                 }

#                 result = compare_codes(gold, pred)

#                 print(f"\n[Example {ex_idx + 1} - Scenario {sc_idx + 1}]")
#                 print(f"- cron            : {result['cron_equal']}  ({result['cron']['gold']} vs {result['cron']['pred']})")
#                 print(f"- period          : {result['period_equal']}  ({result['period']['gold']} vs {result['period']['pred']})")
#                 print(f"- logic equivalent: {result['logic_equivalent']}")
#                 print(f"- script similarity: {result['script_similarity']:.3f}")
#                 print(f"- ast similarity  : {result['ast_similarity']:.3f}")
            



def main():
    model_name = "qwenCoder"

    if model_name == "qwenCoder":
        model_path = "unsloth/Qwen2.5-Coder-7B-bnb-4bit"

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=model_path,
        max_seq_length=8192,
        dtype=None,
        load_in_4bit=True,
    )
    model.load_adapter(f"./models/{model_name}-adapter")
    FastLanguageModel.for_inference(model)

    tokenizer = get_chat_template(tokenizer, chat_template="chatml" if model_name != "gemma3" else "gemma-3", map_eos_token=True)
    tokenizer.add_bos_token = False
    stop_token_ids = get_stop_token_ids(model_name, tokenizer)

    # model_bge = BGEM3FlagModel("./models/bge-m3", use_fp16=False, local_files_only=True)
    # model_sentence = SentenceTransformer('./models/paraphrase-MiniLM-L6-v2')
    model_bge = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)
    model_sentence = SentenceTransformer("paraphrase-MiniLM-L6-v2")

    with open("./ServiceExtraction/integration/service_list_ver1.1.8.txt", "r") as f:
        service_doc = f.read()
    classes = extract_classes_by_name(service_doc)

    for i in range(15, 17):
        if i==1:
            continue
        with open(f"./Testset/TestsetWithDevices_translated/category_{i}.yaml", "r") as f:
            results = []
            data = yaml.safe_load(f)

            for item in data:
                user_command = item["command_translated"]
                user_command_origin = item["command"]

                start_bge = time.time()
                service_selected = set(r["key"] for r in hybrid_recommend(model_bge, user_command_origin, max_k=10))
                service_selected.add("Clock")
                bge_elapsed = time.time() - start_bge

                
                if (i == 13):
                    classes_copy = copy.deepcopy(classes)
                    extra_tags = ["Upper", "Lower", "SectorA", "SectorB", "Wall", "Odd", "Even",]
                    for key in classes.keys():
                        doc = classes[key]
                        lines = doc.splitlines()
                        new_lines = lines[:4] + [f"    #{tag}" for tag in sorted(set(extra_tags))] + lines[4:]
                        classes[key] = "\n".join(new_lines)


                resp, llm_elapsed = run_test_case_unsloth(
                    model, tokenizer, stop_token_ids, model_name, user_command_origin, user_command, classes, service_selected
                )

                if (i == 13):
                    classes = classes_copy 

                print(f"Command: {user_command_origin}")
                print(f"code: {resp}")

                try:
                    code = parse_scenarios(extract_last_code_block(resp))['code']
                except:
                    try:
                        code = parse_scenarios(resp)['code']
                    except:
                        code = [{'name': 'Scenario1', 'cron': '', 'period': -1, 'code': ''}]

                for c in code:
                    code_n = c["code"].strip()
                    code_n = validate_tmp(code_n, classes, list(service_selected), model_sentence)
                    c["code"] = LiteralString(code_n if code_n else "")

                entry = {
                    "command": user_command_origin,
                    "command_translated": user_command,
                    "devices": list(service_selected),
                    "generated_code": code,
                    "model_info": {
                        "elapsed_time": round(llm_elapsed + bge_elapsed, 3),
                        "bge_elapsed_time": round(bge_elapsed, 3),
                        "llm_elapsed_time": round(llm_elapsed, 3)
                    }
                }
                results.append(entry)

        os.makedirs(f"./Testset/Eval_{model_name}/", exist_ok=True)
        with open(f"./Testset/Eval_{model_name}/evaluation_category_{i}.yaml", "w", encoding="utf-8") as out_file:
            yaml.dump(results, out_file, indent=2, allow_unicode=True, sort_keys=False, width=float('inf'))

    del model
    gc.collect()



if __name__ == "__main__":
    main()
    # compare_all("codegemma")
