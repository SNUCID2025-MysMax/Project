# compare_soplang_ir.py

from .soplang_parser_full import parser, lexer
from z3 import *
import json
import difflib

#Soplang 코드를 PLY 기반 파서로 파싱하여 AST return
def parse_soplang(code: str):
    return parser.parse(code, lexer=lexer)

#조건 관련 모든 노드 추출
def extract_logic_expressions(ast):
    logic = []

    def dfs(node):
        if isinstance(node, dict):
            node_type = node.get("type")
            if node_type == "Scenario":
                dfs(node.get("body"))
            elif node_type == "If":
                logic.append(node["condition"])
                dfs(node.get("then"))
                if node.get("else"):
                    dfs(node["else"])
            elif node_type == "WaitUntil":
                if node.get("condition"):
                    logic.append(node["condition"])
            elif node_type == "Block":
                for stmt in node.get("body", []):
                    dfs(stmt)
        elif isinstance(node, list):
            for item in node:
                dfs(item)

    dfs(ast)
    return logic





#Z3(논리식 비교 라이브러리) 를 사용하기 위한 전처리 과정
def condition_to_z3(cond):
    if cond is None or not isinstance(cond, dict):
        return BoolVal(True)

    op_map = {
        ">=": lambda l, r: l >= r,
        "<=": lambda l, r: l <= r,
        "==": lambda l, r: l == r,
        "!=": lambda l, r: l != r,
        ">": lambda l, r: l > r,
        "<": lambda l, r: l < r
    }

    left = cond["left"]
    right = cond["right"]
    op = cond["op"]

    try:
        # 실수형 판단
        if isinstance(right, float):
            l = Real(left) if isinstance(left, str) else left
            r = RealVal(right)
        else:
            l = Int(left) if isinstance(left, str) else left
            r = IntVal(right)

        return op_map[op](l, r)

    except Exception as e:
        #print(f"[Z3 WARN] Failed to convert condition: {cond} → {e}")
        return BoolVal(True)


def are_equivalent(logic1, logic2):
    s = Solver()
    expr1 = And([condition_to_z3(cond) for cond in logic1 if cond])
    expr2 = And([condition_to_z3(cond) for cond in logic2 if cond])
    s.add(expr1 != expr2)
    return s.check() == unsat

def compute_similarity(code1, code2):
    seq = difflib.SequenceMatcher(None, code1, code2)
    return seq.ratio()

def compare_codes(gold: dict, pred: dict):
    # 1. cron, period 정확히 일치 여부 확인
    cron_equal = gold["cron"] == pred["cron"]
    period_equal = gold["period"] == pred["period"]

    # 2. script 파싱 후 AST 비교
    gold_ast = {"type": "Scenario", "body": parse_script_only(gold["script"].replace("\\n", "\n"))}
    pred_ast = {"type": "Scenario", "body": parse_script_only(pred["script"].replace("\\n", "\n"))}
  
    logic1 = extract_logic_expressions(gold_ast)
    logic2 = extract_logic_expressions(pred_ast)

    logic_equiv = are_equivalent(logic1, logic2)
    script_sim = compute_similarity(gold["script"], pred["script"])
    ast_sim = ast_similarity_score(gold_ast, pred_ast)

    return {
        "cron_equal": cron_equal,
        "period_equal": period_equal,
        "cron": {"gold": gold["cron"], "pred": pred["cron"]},
        "period": {"gold": gold["period"], "pred": pred["period"]},
        "logic_equivalent": logic_equiv,
        "script_similarity": round(script_sim, 3),
        "ast_similarity": round(ast_sim, 3)
    }


def parse_script_only(script_code: str):
    return parser.parse(script_code, lexer=lexer)

def parse_script_json(json_data):
    script_code = json_data["script"].replace("\\n", "\n")

    # {}로 감싸서 valid한 statement_list 구성
    wrapped_code = f"{{\n{script_code}\n}}"

    # 파싱 시도
    tree = parser.parse(wrapped_code, lexer=lexer)
    if tree is None:
        raise ValueError(f"파싱 실패: {json_data.get('name', '<unnamed>')}")

    # AST 추출
    body = tree.get("body", [])
    block = body[0] if body and body[0]["type"] == "Block" else None
    ast = block["body"] if block else []

    # 전체 반환
    return {
        "name": json_data.get("name", ""),
        "cron": json_data["cron"],
        "period": json_data["period"],
        "script": json_data["script"],
        "ast": ast
    }

def flatten_ast(node):
    flat = []

    def dfs(n):
        if isinstance(n, dict):
            flat.append(f"DICT:{sorted(n.keys())}")
            for k, v in n.items():
                dfs(v)
        elif isinstance(n, list):
            flat.append("LIST")
            for v in n:
                dfs(v)
        else:
            if isinstance(n, str):
                flat.append(f"VALUE:str={n}")
            elif isinstance(n, (int, float)):
                flat.append(f"VALUE:{type(n).__name__}={n}")
            else:
                flat.append(f"VALUE:{type(n).__name__}")

    dfs(node)
    return flat


def ast_similarity_score(ast1, ast2):
    flat1 = flatten_ast(ast1)
    flat2 = flatten_ast(ast2)
    
    matcher = difflib.SequenceMatcher(None, flat1, flat2)
    return matcher.ratio()

