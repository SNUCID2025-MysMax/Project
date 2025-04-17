import sys
import json
from itertools import product
import re
from soplang_parser_full import parser, lexer
from compare_soplang_ir import extract_logic_expressions

# Soplang 표현식을 현재 context 로 평가
def evaluate_expression(expr, context):
    if isinstance(expr, dict):
        if expr.get("type") == "AttrAccess":
            key = f"{expr['tags'][0]}.{expr['attr']}"
            return context.get(key, 0)
        elif expr.get("type") == "MethodCall":
            # return dummy value
            return f"result_of_{expr['method']}"
    elif isinstance(expr, str):
        val = context.get(expr, expr)
        try:
            if isinstance(val, str) and val.isdigit():
                return int(val)
            elif isinstance(val, str) and '.' in val:
                return float(val)
            else:
                return val
        except:
            return val
    return expr

def convert_type(left, right):
    try:
        if isinstance(right, (int, float)):
            return type(right)(left)
        if isinstance(right, str):
            return str(left)
    except:
        pass
    return left

def evaluate_condition(cond, context):
    if cond is None:
        return True
    if isinstance(cond, dict):
        op = cond.get("op")
        if op in ("and", "or"):
            left = evaluate_condition(cond["left"], context)
            right = evaluate_condition(cond["right"], context)
            return (left and right) if op == "and" else (left or right)
        elif op == "not":
            return not evaluate_condition(cond["expr"], context)
        else:
            left = evaluate_expression(cond["left"], context)
            right = evaluate_expression(cond["right"], context)
            left = convert_type(left, right)
            if op == '>=': return left >= right
            if op == '<=': return left <= right
            if op == '==': return left == right
            if op == '!=': return left != right
            if op == '>': return left > right
            if op == '<': return left < right
    return False

# 블록 내부의 statement 를 순회하여 조건 평가 및 action 실행
def flatten_actions(ir, context, depth=0):
    actions = []

    def visit(node):
        if node["type"] == "Assign":
            val = evaluate_expression(node["value"], context)
            context[node["target"]] = val
            actions.append(("Assign", node["target"], val, depth))

        elif node["type"] == "Action":
            args = [evaluate_expression(arg, context) for arg in node["args"]]
            actions.append(("Action", ','.join(node["target"]), node["service"], tuple(args), depth))

        elif node["type"] == "If":
            if evaluate_condition(node["condition"], context):
                visit(node["then"])
            elif node["else"]:
                visit(node["else"])

        elif node["type"] == "Block":
            for s in node["body"]:
                visit(s)

        elif node["type"] == "WaitUntil":
            ok = evaluate_condition(node["condition"], context)
            actions.append((f"WaitUntil[{'OK' if ok else 'BLOCKED'}]", str(node["condition"]), depth))

        elif node["type"] == "Loop":
            for i in range(3):
                ok = evaluate_condition(node["condition"], context)
                actions.append((f"Loop[{i}]", node.get("time"), ok, depth))
                if ok:
                    visit(node["body"])

    for stmt in ir["body"]:
        visit(stmt)

    return actions



# 조건식을 기반으로 context 조합 생성
def generate_context_from_conditions(logic):
    candidates = {}

    for cond in logic:
        if cond is None or not isinstance(cond, dict): continue
        op = cond.get("op")

        if op in ("and", "or", "not"):
            left = cond.get("left") or cond.get("expr")
            right = cond.get("right") if op != "not" else None
            subconds = [left] + ([right] if right else [])
            sublogic = generate_context_from_conditions(subconds)
            for var, vals in sublogic.items():
                candidates.setdefault(var, set()).update(vals)
            continue

        left = cond["left"]
        if isinstance(left, dict) and left.get("type") == "AttrAccess":
            var = f"{left['tags'][0]}.{left['attr']}"
        else:
            var = left

        val = cond["right"]

        # 숫자형 조건
        if isinstance(val, (int, float)):
            vals = [val - 1, val, val + 1]

        # 문자열 조건
        elif isinstance(val, str):
            if var == "__loop_time__":
                #  시간 문자열에서 숫자와 단위 분리 (예: "1 HOUR" → 1, "HOUR")
                m = re.match(r"(\d+)\s*(\w+)", val)
                if m:
                    base = int(m.group(1))
                    unit = m.group(2)
                    vals = [f"{base} {unit}", f"{base * 5} {unit}", f"{base * 10} {unit}"]
                else:
                    vals = [val]
            else:
                vals = [val]
        else:
            continue

        candidates.setdefault(var, set()).update(vals)

    # 전체 조합 생성
    keys = sorted(candidates.keys())
    value_sets = [sorted(candidates[k]) for k in keys]

    context_variants = []
    for combo in product(*value_sets):
        ctx = {k: v for k, v in zip(keys, combo)}
        context_variants.append(ctx)

    return context_variants


