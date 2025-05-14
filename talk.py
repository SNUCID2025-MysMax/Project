from openai import OpenAI
from dotenv import load_dotenv
import os, sys, re, gc, json
from datetime import datetime
from Grammar.grammar_ver1_1_2 import grammar, grammar_compressed
from Embedding.embedding import hybrid_recommend
from Conversion.conversion import transform_code
from FlagEmbedding import BGEM3FlagModel

from Evaluation.soplang_parser_full import parser, lexer
from Evaluation.soplang_ir_simulator import flatten_actions, generate_context_from_conditions
from Evaluation.compare_soplang_ir import extract_logic_expressions, compare_codes 

# .env 파일에서 환경변수 불러오기
load_dotenv()

# docstring
def extract_classes_by_name(text: str):
    pattern = r'class\s+(\w+)\s*:\s*\n\s+"""(.*?)"""'
    matches = re.finditer(pattern, text, re.DOTALL)

    class_dict = {}
    for match in matches:
        class_name = match.group(1)
        full_class_def = match.group(0)  # 전체 클래스 문자열
        class_dict[class_name] = full_class_def

    return class_dict

with open("./ServiceExtraction/integration/service_list_ver1.1.3.txt", "r") as f:
    service_doc = f.read()
classes = extract_classes_by_name(service_doc)

# Load Embedding
model_dir = os.path.expanduser("./models/bge-m3")
model = BGEM3FlagModel(model_dir, use_fp16=False, local_files_only=True)

# 클라이언트 생성
# 환경 변수에서 API 키 읽기
api_key = os.getenv("apikey")
client = OpenAI(api_key=api_key)

def parse_code_to_ast(script: str):
    wrapped = f"{{\n{script}\n}}"
    return parser.parse(wrapped, lexer=lexer)

results = []
with open("./Testset/test.json", "r") as f:
    data = json.load(f)
    for item in data:
        user_command = item["query"]
        label = item["answer"]

        service_selected = set(i["key"] for i in hybrid_recommend(model, user_command, max_k=7))
        service_selected.add("Clock")
        service_doc = "\n".join([classes[i] for i in service_selected])

        current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        
        prompt = f"# Devices\n{service_doc}\n\n# User Command\ncommand: {user_command}\n\n# Current Time\ncurrent: {current_time}"

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": grammar},
                {"role": "user", "content": prompt},
            ]
        )

        resp = response.choices[0].message.content
        print("응답:\n", resp)
        print("-"*30)
        code = transform_code(resp)
        print("변환된 코드:\n", code)
        print("-"*30)

        # print("모델:", response.model)
        # print("생성 시각:", response.created)
        # print("Finish Reason:", response.choices[0].finish_reason)
        # print("토큰 사용량:")
        # print(" - prompt:", response.usage.prompt_tokens)
        # print(" - completion:", response.usage.completion_tokens)
        # print(" - total:", response.usage.total_tokens)
        # print("="*30)

        entry = {
            "user_command": user_command,
            "devices": service_selected,
            "generated_code": resp,
            "transformed_code": code,
            "label": label,
            "compare_results": [],
            "model_info": {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            }
        }

        ## dummies
        # entry = {"compare_results":[]}

        # code = [
        #     {"name": "Scenario1", "cron": "*/1 * * * *", "period": 180000, "code": "\nbutton_state = (#Button).button_button\nif (button_state != 'pushed') {\n    (#Button).switch_toggle()\n}\n"},
        #     {"name": "Scenario2", "cron": "*/1 * * * *", "period": 300000, "code": "\nac_state = (#AirConditioner).switch_switch\nif (ac_state == 'off') {\n    (#AirConditioner).switch_on()\n} else if (ac_state == 'on') {\n    (#AirConditioner).switch_off()\n}\n"}
        # ]

        entry["len_check"] = {
            "len_generated_code": len(code),
            "len_label_code": len(label),
            "len_is_equal": len(code) == len(label)
        }

        # Syntax 체크
        for c in code:
            try:
                parse_code_to_ast(c)
            except Exception as e:
                print(f"Parse failed: {e}")  
                


        compare_result = {}
        
        for i, (gen, gold) in enumerate(zip(code, label), start=1):
            print(f"\n[Test{i}]")

            gold_wrapped = {
                "name": gold["name"],
                "cron": gold["cron"],
                "period": gold["period"],
                "script": gold["code"]
            }

            gen_wrapped = {
                "name": gen["name"],
                "cron": gen["cron"],
                "period": gen["period"],
                "script": gen["code"]
            }

            result = compare_codes(gold_wrapped, gen_wrapped)

            compare_result = {
                "scenario": gold["name"],
                "cron_equal": result['cron_equal'],
                "period_equal": result['period_equal'],
                "ast_similarity": result['ast_similarity'],
                "script_similarity": result['script_similarity'],
                "mismatches": []
            }

            # print(f"- cron : {result['cron_equal']}")
            # print(f"- period : {result['period_equal']}")
            # print(f"- ast_similarity: {result['ast_similarity']:.3f}")
            # print(f"- script similarity: {result['script_similarity']:.3f}")
            # print("\n→ Simulated Action Traces:")
            try:
                gold_ast = parse_code_to_ast(gold["code"])
                gen_ast = parse_code_to_ast(gen["code"])

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
                            # print(f"\n❌ MISMATCH @ Context #{ctx_idx+1}, Step {j}")
                            # print(f"→ Variables: {ctx}")
                            # print(f"→ Gold Action: {g}")
                            # print(f"→ Pred Action: {p}")
                            
                            compare_result["mismatches"].append({
                                "context_index": ctx_idx + 1,
                                "step": j,
                                "variables": ctx,
                                "gold_action": g,
                                "pred_action": p
                            })

            except Exception as e:
                # print(f"❌ Simulation failed: {e}")      
                compare_result["simulation_error"] = str(e)
            
            entry["compare_results"].append(compare_result)
    results.append(entry)

# 저장하기
with open("./Testset/evaluation_results.json", "w", encoding="utf-8") as out_file:
    json.dump(results, out_file, indent=2, ensure_ascii=False)
    
del model
gc.collect()