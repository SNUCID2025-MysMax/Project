import os, sys, re, gc, json, time, pprint
from datetime import datetime
from Grammar.grammar_ver1_5_1 import grammar
from Embedding.embedding import hybrid_recommend
from FlagEmbedding import BGEM3FlagModel

from Testset.joi_extraction import parse_scenarios
from Evaluation.soplang_parser_full import parser, lexer
from Evaluation.soplang_ir_simulator import flatten_actions, generate_context_from_conditions
from Evaluation.compare_soplang_ir import extract_logic_expressions, compare_codes 

import ollama

with open("./Grammar/SoP_Lang_Description.md", "r") as f:
    description = f.read()
with open("./Grammar/grammar_ver1_5_1_inst.md", "r") as f:
    inst = f.read()

# docstring
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

def parse_code_to_ast(script: str):
    try:
        wrapped = f"{{\n{script}\n}}"
        return parser.parse(wrapped, lexer=lexer)
    except Exception as e:
        print(f"Parse failed: {e}")  

def run_test_case(model, model_bge, user_command, classes, use_stream=True):

    start_time = time.time()

    service_selected = set(i["key"] for i in hybrid_recommend(model_bge, user_command, max_k=7))
    service_elapsed = time.time() - start_time
    service_selected.add("Clock")

    # service_doc = "\n".join([classes[i] for i in service_selected])
    service_doc = "#Devices\n"+"\n".join([json.dumps(classes[i]) for i in service_selected])
    
    prompt = f"Generate SoP Lang code for \"{user_command}\""

    role = "user"

    try:
        if use_stream:
            response = ollama.chat(
                model=model,
                messages=[
                    {"role": role, "content": description},
                    {"role": role, "content": grammar},
                    {"role": role, "content": service_doc},
                    {"role": role, "content": inst},
                    {"role": "user", "content": prompt},
                ],
                stream=True
            )

            full_response = ""
            last_chunk = None
            for chunk in response:
                last_chunk = chunk
                if 'message' in chunk and 'content' in chunk['message']:
                    content = chunk['message']['content']
                    full_response += content
                    print(content, end='', flush=True)

            elapsed = time.time() - start_time

            info = {
                "elapsed_time": round(elapsed, 3),
                "bge_elapsed_time": round(service_elapsed, 3),
                "llm_elapsed_time": round(elapsed - service_elapsed, 3),
                "prompt_tokens": last_chunk.get("prompt_eval_count", None) if last_chunk else None,
                "generated_tokens": last_chunk.get("eval_count", None) if last_chunk else None,
            }
        else:
            response = ollama.chat(
                model=model,
                messages=[
                    {"role": role, "content": description},
                    {"role": role, "content": grammar},
                    {"role": role, "content": service_doc},
                    {"role": role, "content": inst},
                    {"role": "user", "content": prompt},
                ]
            )
            full_response = response['message']['content']
            elapsed = time.time() - start_time

            info = {
                "elapsed_time":round(elapsed, 3),
                "bge_elapsed_time": round(service_elapsed, 3),
                "llm_elapsed_time": round(elapsed - service_elapsed, 3),
                "prompt_tokens": response.get("prompt_eval_count", None),
                "generated_tokens": response.get("eval_count", None),
            }
        return full_response.strip(), service_selected, info

    except Exception as e:
        print(e)
        return f"Error: {e}", None, {"elapsed_time": None, "prompt_tokens": None, "generated_tokens": None}

def evaluate_pair(gold, gen):
    compare_result = {
        "scenario": gold["name"],
        "cron_equal": None,
        "period_equal": None,
        "ast_similarity": None,
        "script_similarity": None,
        "mismatches": []
    }

    # 메트릭 비교
    result = compare_codes(gold, gen)
    compare_result.update({
        "cron_equal": result['cron_equal'],
        "period_equal": result['period_equal'],
        "ast_similarity": result['ast_similarity'],
        "script_similarity": result['script_similarity']
    })

    try:
        gold_ast = parse_code_to_ast(gold["script"])
        gen_ast = parse_code_to_ast(gen["script"])

        logic = extract_logic_expressions(gold_ast)
        contexts = generate_context_from_conditions(logic)

        for ctx_idx, ctx in enumerate(contexts):
            gold_trace = flatten_actions(gold_ast, ctx.copy())
            gen_trace = flatten_actions(gen_ast, ctx.copy())

            gold_actions = [a for a in gold_trace if a[0] == "Action"]
            gen_actions = [a for a in gen_trace if a[0] == "Action"]

            max_len = max(len(gold_actions), len(gen_actions))
            for j in range(max_len):
                g = gold_actions[j] if j < len(gold_actions) else "❌ Missing"
                p = gen_actions[j] if j < len(gen_actions) else "❌ Missing"

                if g != p:
                    compare_result["mismatches"].append({
                        "context_index": ctx_idx + 1,
                        "step": j,
                        "variables": ctx,
                        "gold_action": g,
                        "pred_action": p
                    })

    except Exception as e:
        compare_result["simulation_error"] = str(e)

    return compare_result

def main():
    # select sllm
    model = "exaone-deep:7.8B"
    model = "qwen2.5-coder:7b"
    model = "llama3.2:3b"
    model = "codellama:7b"

    # Load Embedding
    model_dir = os.path.expanduser("./models/bge-m3")
    model_bge = BGEM3FlagModel(model_dir, use_fp16=False, local_files_only=True)
    hybrid_recommend(model_bge, "에어컨", max_k=7)
    print("Embedding loaded")

    # Load llm
    response = ollama.chat(
        model = model,
        messages=[{"role":"system", "content":"Do not print anything."},
                  {"role": "user", "content": "hi"}],
    )
    print("LLM loaded")

    # 태그, 서비스 목록 불러오기

    # with open("./ServiceExtraction/integration/service_list_ver1.1.7.txt", "r") as f:
    #     service_doc = f.read()
    # classes = extract_classes_by_name(service_doc)

    with open("./ServiceExtraction/integration/service_list_ver1.5.3.json", "r") as f:
        classes = json.load(f)

    results = []

    with open("./Testset/test.json", "r") as f:
        data = json.load(f)
        for item in data:
            user_command = item["query"]
            # label = item["answer"]
            
            resp, service_selected, info = run_test_case(
                model, model_bge, user_command, classes, False
            )
            print(f"#명령어: {user_command}")
            print(f"#총 응답 시간 : {info['elapsed_time']}초")
            print(f"#디바이스 추출: {service_selected} ({info["bge_elapsed_time"]}초)")
            print(f"#모델 응답 시간: {info["llm_elapsed_time"]}초")
            print("#응답:\n", resp)
            print("="*30)
            
        #     resp = extract_last_python_block(resp)
        #     print(resp)
        #     code = ""
        #     try:
        #         code = parse_scenarios(resp)
        #     except:
        #         code = ""
        #     print("변환된 코드:\n", code)
        #     print("-"*30)

        #     entry = {
        #         "user_command": user_command,
        #         "devices": service_selected,
        #         "generated_code": resp,
        #         "label": label,
        #         "compare_results": [],
        #         "model_info": {
        #             "prompt_tokens": info["prompt_tokens"],
        #             "generated_tokens": info["generated_tokens"],
        #             "elapsed_time": info["elapsed_time"],
        #         }
        #     }

        #     entry["len_check"] = {
        #         "len_generated_code": len(code),
        #         "len_label_code": len(label),
        #         "len_is_equal": len(code) == len(label)
        #     }

        #     # Syntax 체크
        #     entry["syntax_errors"] = []
        #     for c in code:
        #         try:
        #             parse_code_to_ast(c)
        #         except Exception as e:
        #             entry["syntax_errors"].append(str(e))
                    
            
        #     for i, (gen, gold) in enumerate(zip(code, label), start=1):
        #         gold_wrapped = {
        #             "name": gold["name"],
        #             "cron": gold["cron"],
        #             "period": gold["period"],
        #             "script": gold["code"]
        #         }

        #         gen_wrapped = {
        #             "name": gen["name"],
        #             "cron": gen["cron"],
        #             "period": gen["period"],
        #             "script": gen["code"]
        #         }

        #         result = evaluate_pair(gold_wrapped, gen_wrapped)
        #         entry["compare_results"].append(result)
        # results.append(entry)

    # 저장하기
    with open("./Testset/evaluation_results.json", "w", encoding="utf-8") as out_file:
        json.dump(results, out_file, indent=2, ensure_ascii=False)
        
    del model
    gc.collect()


if __name__ == "__main__":
    main()
