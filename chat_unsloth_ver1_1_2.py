import os, sys, re, gc, yaml, time, json, copy
from datetime import datetime
import concurrent.futures

# from unsloth import FastLanguageModel
# from unsloth.chat_templates import get_chat_template
# from transformers import AutoTokenizer
# from peft import PeftModel

# from FlagEmbedding import BGEM3FlagModel
# from Embedding.embedding import hybrid_recommend
# from Grammar.grammar_ver1_1_5 import grammar
# from Testset.joi_extraction_tool import parse_scenarios, extract_last_code_block
# from Validation.validate import validate_tmp
# from sentence_transformers import SentenceTransformer

from yaml.representer import SafeRepresenter

from Evaluation.compare_soplang_ir import  compare_codes

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


def compare_all(model_name: str):
    gold_path = f"./Testset/Testset"
    pred_path = f"./Testset/Eval_{model_name}"
    
    results_summary = []
    all_scores = []
    
    def extract_number(filename):
        match = re.search(r'(\d+)', filename)
        return int(match.group(1)) if match else float('inf')
    files = sorted(
        [f for f in os.listdir(gold_path) if f.endswith(".yaml")],
        key=extract_number
    )                                   
    
    for file_idx, file in enumerate(files):
        file_results = []
        file_scores = []
        
        with open(os.path.join(gold_path, file), 'r', encoding='utf-8') as f1:
            gold_data = yaml.safe_load(f1)
        
        with open(os.path.join(pred_path, f"evaluation_{file}"), 'r', encoding='utf-8') as f2:
            pred_data = yaml.safe_load(f2)
        
        for ex_idx, (gold_item, pred_item) in enumerate(zip(gold_data, pred_data)):
            ex_id = f"ex{file_idx}-{ex_idx + 1}"
            gold = gold_item["code"][0] if gold_item["code"] else {
                "name": "Scenario1", "cron": "", "period": -1, "code": ""
            }
            pred_list = pred_item.get("generated_code", [])
            if isinstance(pred_list, dict):
                pred_list = [pred_list]
            elif not isinstance(pred_list, list):
                pred_list = []

            pred = pred_list[0] if pred_list else {
                "name": "Scenario1", "cron": "", "period": -1, "code": ""
            }
                
            label = {
                "name": gold["name"],
                "cron": gold["cron"],
                "period": gold["period"],
                "script": gold["code"]
            }
            model  = {
                "name": pred["name"],
                "cron": pred["cron"],
                "period": pred["period"],
                "script": pred["code"]
            }
            
            result = compare_codes(label, model)
            
            score = 0
            
            cron_status = "equal" if result["cron_equal"] else "different"
            period_status = "equal" if result["period_equal"] else "different"
            code_score = round(result["ast_similarity"], 3)
            
            if result["cron_equal"]:
                score += 25
            if result["period_equal"]:
                score += 25
            score += int(code_score * 50)
            status = f"(cron: {cron_status},  period: {period_status}, code: {code_score:.2f})"
            
            diff_block = {}
            if not result["cron_equal"]:
                diff_block["cron"] = f"model = {model['cron']}, label = {label['cron']}"
            if not result["period_equal"]:
                diff_block["period"] = f"model = {model['period']}, label = {label['period']}"
            if result["ast_similarity"] < 1.0:
                diff_block["code"] = f"ast_similarity = {code_score}"

            file_scores.append(score)
            file_results.append({
                "id": ex_id,
                "score": f"{score} {status}",
                "diff": diff_block
            })
        avg_file_score = sum(file_scores) / len(file_scores)
        results_summary.extend(file_results)
        results_summary.append({
            "id": f"{file.replace('.yaml', '')}-avg",
            "score": f"{avg_file_score:.1f} (average of {len(file_scores)} examples)"
        })
        all_scores.extend(file_scores)
        
    overall_avg = sum(all_scores) / len(all_scores)
    results_summary.append({
        "id": "overall-avg",
        "score": f"{overall_avg:.1f} (average of {len(all_scores)} total examples)",
    })
    
    with open(f"./Testset/Eval_{model_name}/comparison_summary.yaml", "w", encoding="utf-8") as out_f:
        yaml.dump(results_summary, out_f, allow_unicode=True, sort_keys=False)
            



def main():
    model_name = "codegemma"

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=f"./models/{model_name}-model",
        max_seq_length=8192,
        dtype=None,
        load_in_4bit=True,
    )
    model.load_adapter(f"./models/{model_name}-adapter-250605")
    FastLanguageModel.for_inference(model)

    tokenizer = get_chat_template(tokenizer, chat_template="chatml" if model_name != "gemma3" else "gemma-3", map_eos_token=True)
    tokenizer.add_bos_token = False
    stop_token_ids = get_stop_token_ids(model_name, tokenizer)

    model_bge = BGEM3FlagModel("./models/bge-m3", use_fp16=False, local_files_only=True)
    model_sentence = SentenceTransformer('./models/paraphrase-MiniLM-L6-v2')

    with open("./ServiceExtraction/integration/service_list_ver1.1.8.txt", "r") as f:
        service_doc = f.read()
    classes = extract_classes_by_name(service_doc)

    for i in range(0, 1):
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
    #main()
    compare_all("codegemma")
