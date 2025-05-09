from openai import OpenAI
from dotenv import load_dotenv
import os, sys, re, gc
from datetime import datetime
from grammar import grammar, grammar_compressed
import tiktoken
from embedding import hybrid_recommend
from conversion import transform_code
from FlagEmbedding import BGEM3FlagModel

sys.path.append("./Evaluation")
from soplang_parser_full import parser, lexer
from soplang_ir_simulator import flatten_actions, generate_context_from_conditions
from compare_soplang_ir import extract_logic_expressions, compare_codes 


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

with open("0.1.3_docstring_v3.txt", "r", encoding="utf-8") as f:
    service_doc = f.read()
classes = extract_classes_by_name(service_doc)

# Load Embedding
model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=False)

queries = [
    "3분마다 알람을 울려줘. 5분마다 에어컨 스위치를 토글해.",
]

for user_command in queries:
    service_selected = set(i["key"] for i in hybrid_recommend(model, user_command, max_k=7))
    service_selected.add("Clock")
    service_doc = "\n".join([classes[i] for i in service_selected])

    current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
    prompt = f"# Devices\n{service_doc}\n\n# User Command\ncommand: {user_command}\n\n# Current Time\ncurrent: {current_time}"
    with open("prompt.txt", "w") as f:
        f.write(prompt)
    
    # encoding = tiktoken.encoding_for_model("gpt-4")
    # text = f"{grammar}\n---\n{service_doc}\ncommand: {user_command}\ncurrent: {current_time}"
    # num_tokens = len(encoding.encode(text))
    # print(f"총 토큰 수: {num_tokens}")

    # 환경 변수에서 API 키 읽기
    api_key = os.getenv("apikey")

    # 클라이언트 생성
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": grammar_compressed},
            {"role": "user", "content": prompt},
        ]
    )

    resp = response.choices[0].message.content
    print("응답:\n", resp)
    print("-"*30)
    code = transform_code(resp)
    # ---------------------------------- #
    # Todo()
    # code: [{'name': 'Scenario1', 'cron': '*/1 * * * *', 'period': 180000, 'code': "\nbutton_state = (#Button).button_button\nif (button_state != 'pushed') {\n    (#Button).switch_toggle()\n}\n"},
    # {'name': 'Scenario2', 'cron': '*/1 * * * *', 'period': 300000, 'code': "\nac_state = (#AirConditioner).switch_switch\nif (ac_state == 'off') {\n    (#AirConditioner).switch_on()\n} else if (ac_state == 'on') {\n    (#AirConditioner).switch_off()\n}\n"}]
    # 리스트에 담긴 시나리오 별로 평가 필요
    # label : 정답 code 라고 가정
    def parse_code_to_ast(script: str):
        wrapped = f"{{\n{script}\n}}"
        return parser.parse(wrapped, lexer=lexer)
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

        print(f"- cron : {result['cron_equal']}")
        print(f"- period : {result['period_equal']}")
        print(f"- ast_similarity: {result['ast_similarity']:.3f}")
        print(f"- script similarity: {result['script_similarity']:.3f}")
        print("\n→ Simulated Action Traces:")
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
                    print(f"\n❌ MISMATCH @ Context #{ctx_idx+1}, Step {j}")
                    print(f"→ Variables: {ctx}")
                    print(f"→ Gold Action: {g}")
                    print(f"→ Pred Action: {p}")

    except Exception as e:
        print(f"❌ Simulation failed: {e}")      

    # ---------------------------------- #

    print("변환된 코드:\n", code)
    print("-"*30)

    print("모델:", response.model)
    print("생성 시각:", response.created)
    print("Finish Reason:", response.choices[0].finish_reason)
    print("토큰 사용량:")
    print(" - prompt:", response.usage.prompt_tokens)
    print(" - completion:", response.usage.completion_tokens)
    print(" - total:", response.usage.total_tokens)
    print("="*30)
del model
gc.collect()