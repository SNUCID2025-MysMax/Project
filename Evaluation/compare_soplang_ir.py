# compare_soplang_ir.py

from soplang_parser_full import parser, lexer
from z3 import *
import json
import difflib

#Soplang 코드를 PLY 기반 파서로 파싱하여 AST return
def parse_soplang(code: str):
    return parser.parse(code, lexer=lexer)

#조건 관련 모든 노드 추출
def extract_logic_expressions(ast):
    logic = []

    def dfs(node, path="root"):
        if isinstance(node, dict):
            node_type = node.get("type")
            if node_type == "Scenario":
                dfs(node.get("body"), path + ".body")
            elif node_type == "If":
                logic.append(node["condition"])
                dfs(node.get("then"), path + ".then")
                if node.get("else"): dfs(node["else"], path + ".else")
            elif node_type == "Loop":
                if node.get("condition"):
                    logic.append(node["condition"])
                if node.get("time"):
                    logic.append({
                        "left": "__loop_time__",
                        "op": "==",
                        "right": node["time"]
                    })
                dfs(node.get("body"), path + ".body")

            elif node_type == "WaitUntil":
                if node.get("condition"):
                    logic.append(node["condition"])

            elif node_type == "Block":
                for i, stmt in enumerate(node.get("body", [])):
                    dfs(stmt, path + f".body[{i}]")

        elif isinstance(node, list):
            for i, item in enumerate(node):
                dfs(item, path + f"[{i}]")

    dfs(ast)
    return logic




#Z3(논리식 비교 라이브러리) 를 사용하기 위한 전처리 과정
def condition_to_z3(cond):
    if cond is None:
        return BoolVal(True)

    if not isinstance(cond, dict):
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

    if isinstance(right, str):
        return BoolVal(True)

    l = Int(left) if isinstance(left, str) else left
    r = IntVal(right)
    return op_map[op](l, r)


def are_equivalent(logic1, logic2):
    s = Solver()
    expr1 = And([condition_to_z3(cond) for cond in logic1 if cond])
    expr2 = And([condition_to_z3(cond) for cond in logic2 if cond])
    s.add(expr1 != expr2)
    return s.check() == unsat

def compute_similarity(code1, code2):
    seq = difflib.SequenceMatcher(None, code1, code2)
    return seq.ratio()

def compare_codes(code1: str, code2: str):
    ast1 = parse_soplang(code1)
    ast2 = parse_soplang(code2)

    logic1 = extract_logic_expressions(ast1)
    logic2 = extract_logic_expressions(ast2)

    equivalent = are_equivalent(logic1, logic2)
    similarity = compute_similarity(code1, code2)

    return {
        "equivalent": equivalent,
        "similarity": round(similarity, 3),
        "logic1": logic1,
        "logic2": logic2
    }
