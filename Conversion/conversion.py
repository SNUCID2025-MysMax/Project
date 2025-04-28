import re, ast
import json

def transform_code(code):
    tree = ast.parse(code)
    result_total = []
    result = {}
    statements = []

    def custom_unparse_condition(node):
        if isinstance(node, ast.BoolOp):
            op = " and " if isinstance(node.op, ast.And) else " or "
            return "(" + op.join(custom_unparse_condition(value) for value in node.values) + ")"
        elif isinstance(node, ast.Compare):
            return "(" + ast.unparse(node).strip() + ")"
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            return "(not " + custom_unparse_condition(node.operand) + ")"
        else:
            return "(" + ast.unparse(node).strip() + ")"

    def extract_statements(body, prefix=""):
        for stmt in body:
            if isinstance(stmt, ast.If):
                # if 문
                condition = ast.unparse(stmt.test).strip()
                # condition = custom_unparse_condition(stmt.test)
                statements.append(f"{prefix}if ({condition}) {{")
                extract_statements(stmt.body, prefix=prefix + "    ")
                orelse = stmt.orelse
                while orelse:
                    first = orelse[0]
                    if isinstance(first, ast.If):
                        condition = ast.unparse(first.test).strip()
                        # condition = custom_unparse_condition(first.test)
                        statements.append(f"{prefix}}} else if ({condition}) {{")
                        extract_statements(first.body, prefix=prefix + "    ")
                        orelse = first.orelse
                    else:
                        statements.append(f"{prefix}}} else {{")
                        extract_statements([first], prefix=prefix + "    ")
                        break
                statements.append(f'{prefix}}}')
            else:
                # 일반 문장
                line = ast.unparse(stmt).strip()
                statements.append(f"{prefix}{line}")

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_name = node.name

            result = {}
            statements = [""]
            result["name"] = class_name

            for item in node.body:
                # __init__ 메서드
                if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                    for sub_item in item.body:
                        dct = {sub_item.targets[0].attr:ast.literal_eval(sub_item.value)}
                        for key in dct.keys():
                            if key in ["cron", "period"]:
                                result[key] = dct[key]
                            else:
                                statements.append(f"{key} := {dct[key]}")

                if isinstance(item, ast.FunctionDef) and item.name == "run":
                    extract_statements(item.body)

            code = '\n'.join(statements+[""])
            
            def replace_tags_arguments(text):
                pattern = r'Tags\((.*?)\)'

                def replacer(match):
                    inner = match.group(1)
                    parts = [p.strip().strip('"').strip("'") for p in inner.split(',')]
                    new_text = ' '.join(f"#{p}" for p in parts)
                    return f"({new_text})"

                replaced = re.sub(pattern, replacer, text)
                return replaced

            def replace_all_any_parentheses(text):
                result = ''
                i = 0
                while i < len(text):
                    if text[i:i+4] in ('All(', 'Any('):
                        func_name = text[i:i+3]
                        result += func_name.lower()
                        i += 4
                        count = 1
                        start = i
                        while i < len(text) and count > 0:
                            if text[i] == '(':
                                count += 1
                            elif text[i] == ')':
                                count -= 1
                            i += 1
                        result += text[start:i-1]
                    else:
                        result += text[i]
                        i += 1
                return result

            
            code = replace_all_any_parentheses(replace_tags_arguments(code)).replace('self.', '').replace('wait_until', 'wait until')

            result["code"] = code
            result_total.append(result)

    return(result_total)



if __name__ == "__main__":
    
    # 변환할 파이썬 코드 예시
    example = """class Scenario1:
    def __init__(self):
        self.cron = "now"
        self.period = -1
        self.var = False  # Whether alarm was triggered

    def run(self):
        if Any(Tags("Window").windowControl_window == "open"):
            All(Tags("Window").windowControl_close())

            if Tags("Clock").clock_hour < 12:
                All(Tags("Alarm").alarm_both())
                self.var = True

                ac_mode = Tags("AirConditioner").airConditionerMode_airConditionerMode
                All(Tags("AirConditioner").switch_on())
                All(Tags("AirConditioner").airConditionerMode_setTemperature(15))
                All(Tags("AirConditioner").airConditionerMode_setAirConditionerMode("auto"))

                if ac_mode == "auto":
                    All(Tags("AirConditioner").switch_off())
"""
    print(json.dumps(transform_code(example), indent=2, ensure_ascii=False).replace("\\n","\n"))