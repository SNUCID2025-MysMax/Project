from openai import OpenAI
from dotenv import load_dotenv
import os, sys, re, gc, json, yaml, copy
from datetime import datetime
from Grammar.grammar_ver1_1_4 import grammar
from Embedding.embedding import hybrid_recommend
from FlagEmbedding import BGEM3FlagModel

from Testset.tools import print_yaml
from Testset.joi_extraction_tool import parse_scenarios
from Evaluation.soplang_parser_full import parser, lexer
from Evaluation.soplang_ir_simulator import flatten_actions, generate_context_from_conditions
from Evaluation.compare_soplang_ir import extract_logic_expressions, compare_codes 

import yaml
from yaml.representer import SafeRepresenter

class LiteralString(str):
    pass

def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

yaml.add_representer(LiteralString, literal_str_representer)

class QuotedString(str):
    pass

def quoted_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

# docstring
def extract_classes_by_name(text: str):
    pattern = r'Device\s+(\w+)\s*:\s*\n\s+"""(.*?)"""'
    matches = re.finditer(pattern, text, re.DOTALL)

    class_dict = {}
    for match in matches:
        class_name = match.group(1)
        full_class_def = match.group(0)  # 전체 클래스 문자열
        class_dict[class_name] = full_class_def

    return class_dict


def parse_code_to_ast(script: str):
    wrapped = f"{{\n{script}\n}}"
    return parser.parse(wrapped, lexer=lexer)

def extract_last_code_block(text):
    pattern = r"```(?:.*?\n)?(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches[-1] if matches else None


def main():
    # .env 파일에서 환경변수 불러오기
    load_dotenv()

    # Load Embedding
    model_dir = os.path.expanduser("./models/bge-m3")
    model = BGEM3FlagModel(model_dir, use_fp16=False, local_files_only=True)

    with open("./ServiceExtraction/integration/service_list_ver1.1.7.txt", "r") as f:
        service_doc = f.read()
    classes = extract_classes_by_name(service_doc)

    # 클라이언트 생성
    # 환경 변수에서 API 키 읽기
    api_key = os.getenv("apikey")
    client = OpenAI(api_key=api_key)

    for i in range(3, 4):
        file_name = f"category_{i}.yaml"

        example_file = f"./Testset/Testset/{file_name}"

        examples = f"# Examples for this category\n{print_yaml(example_file)}\n"

        results = []
        with open(f"./Testset/Testset/{file_name}", "r") as f:
            data = yaml.safe_load(f)

            for idx, item in enumerate(data):
                # 1~5번만
                if idx >= 5:
                    break

                user_command = item["command"]
                label = item["code"]

                service_selected = set(i["key"] for i in hybrid_recommend(model, user_command, max_k=7))
                service_selected.add("Clock")
                service_doc = "\n".join([classes[i] for i in service_selected])
                
                current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")

                prompt = f"Current Time: {current_time}\nGenerate SoP Lang code for \"{user_command}\""

                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": grammar},
                        {"role": "system", "content": service_doc},
                        {"role": "system", "content": examples},
                        {"role": "user", "content": prompt},
                    ]
                )

                resp = response.choices[0].message.content
                try:
                    code = parse_scenarios(extract_last_code_block(resp))['code']
                except:
                    try:
                        code = parse_scenarios(resp)['code']
                    except:
                        code = [{'name': 'Scenario1', 'cron': '', 'period': -1, 'code': '(#AirConditioner).switch_on()\n'}]
                
                # print("응답:\n", resp)
                # print("-"*30)
                # print("변환된 코드:\n", code)
                # print("-"*30)

                code_for_yaml = copy.deepcopy(code)
                for c in code_for_yaml:
                    c["code"] = LiteralString(c["code"])

                label_for_yaml = copy.deepcopy(label)
                for l in label_for_yaml:
                    l["code"] = LiteralString(l["code"])

                entry = {
                    "command": user_command,
                    "devices": list(service_selected),
                    "generated_code": LiteralString(resp),
                    "transformed_code": code_for_yaml,
                    "label": label_for_yaml,
                    "compare_results": [],
                    "model_info": {
                        "prompt_tokens": response.usage.prompt_tokens,
                        "completion_tokens": response.usage.completion_tokens,
                        "total_tokens": response.usage.total_tokens
                    }
                }

                # # dummies
                # entry = {"compare_results":[]}

                # # code = [
                # #     {"name": "Scenario1", "cron": "*/1 * * * *", "period": 180000, "code": "\nbutton_state = (#Button).button_button\nif (button_state != 'pushed') {\n    (#Button).switch_toggle()\n}\n"},
                # #     {"name": "Scenario2", "cron": "*/1 * * * *", "period": 300000, "code": "\nac_state = (#AirConditioner).switch_switch\nif (ac_state == 'off') {\n    (#AirConditioner).switch_on()\n} else if (ac_state == 'on') {\n    (#AirConditioner).switch_off()\n}\n"}
                # # ]

                # entry["len_check"] = {
                #     "len_generated_code": len(code),
                #     "len_label_code": len(label),
                #     "len_is_equal": len(code) == len(label)
                # }

                # # Syntax 체크
                # for c in code:
                #     try:
                #         parse_code_to_ast(c)
                #     except Exception as e:
                #         print(f"Parse failed: {e}")  

                # compare_result = {}
                
                # for i, (gen, gold) in enumerate(zip(code, label), start=1):
                #     print(f"\n[Test{i}]")
                #     print(gen, gold)

                #     gold_wrapped = {
                #         "name": gold["name"],
                #         "cron": gold["cron"],
                #         "period": gold["period"],
                #         "script": gold["code"]
                #     }

                #     gen_wrapped = {
                #         "name": gen["name"],
                #         "cron": gen["cron"],
                #         "period": gen["period"],
                #         "script": gen["code"]
                #     }

                #     result = compare_codes(gold_wrapped, gen_wrapped)

                #     compare_result = {
                #         "scenario": gold["name"],
                #         "cron_equal": result['cron_equal'],
                #         "period_equal": result['period_equal'],
                #         "ast_similarity": result['ast_similarity'],
                #         "script_similarity": result['script_similarity'],
                #         "mismatches": []
                #     }

                #     try:
                #         gold_ast = parse_code_to_ast(gold["code"])
                #         gen_ast = parse_code_to_ast(gen["code"])

                #         logic = extract_logic_expressions(gold_ast)
                #         contexts = generate_context_from_conditions(logic)

                #         for ctx_idx, ctx in enumerate(contexts):
                #             gold_trace = flatten_actions(gold_ast, ctx.copy())
                #             gen_trace = flatten_actions(gen_ast, ctx.copy())

                #             gold_actions = [a for a in gold_trace if a[0] == "Action"]
                #             gen_actions = [a for a in gen_trace if a[0] == "Action"]

                #             max_len = max(len(gold_actions), len(gen_actions))
                #             for j in range(max_len):
                #                 g = gold_actions[j] if j < len(gold_actions) else "❌ Missing"
                #                 p = gen_actions[j] if j < len(gen_actions) else "❌ Missing"

                #                 if g != p:
                                    
                #                     compare_result["mismatches"].append({
                #                         "context_index": ctx_idx + 1,
                #                         "step": j,
                #                         "variables": ctx,
                #                         "gold_action": g,
                #                         "pred_action": p
                #                     })

                #     except Exception as e:
                #         # print(f"❌ Simulation failed: {e}")      
                #         compare_result["simulation_error"] = str(e)
                    
                #     entry["compare_results"].append(compare_result)
                results.append(entry)

        # 저장하기
        with open(f"./Testset/Eval_gpt/evaluation_{file_name}", "w", encoding="utf-8") as out_file:
            yaml.dump(results, out_file, indent=2, allow_unicode=True, sort_keys=False, width=float('inf'))
        
    del model
    gc.collect()


if __name__ == "__main__":
    main()
