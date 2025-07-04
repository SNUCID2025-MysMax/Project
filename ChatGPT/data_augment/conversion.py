import re, ast, astor
import json

def transform_code(code):
    code = code.strip()
    code = code.replace("\"", "'")
    if code[0] == "'":
        code = code[1:-1]
    elif code.startswith('```python'):
        code = code[9:-3]
    code = code.strip()
    tree = ast.parse(code)
    result_total = []
    result = {}
    statements = []

    def replace_tags_arguments(text):
        pattern = r'Tags\((.*?)\)'

        def replacer(match):
            inner = match.group(1)
            parts = [p.strip().strip('"').strip("'") for p in inner.split(',')]
            new_text = ' '.join(f"#{p}" for p in parts)
            return f"({new_text})"

        replaced = re.sub(pattern, replacer, text)
        return replaced

    def custom_unparse_condition(node):
        if isinstance(node, ast.BoolOp):
            op = " and " if isinstance(node.op, ast.And) else " or "
            return "(" + op.join(custom_unparse_condition(value) for value in node.values) + ")"
        elif isinstance(node, ast.Compare):
            return "(" + astor.to_source(node).strip().replace("\n", "") + ")"
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            return "(not " + custom_unparse_condition(node.operand) + ")"
        else:
            return "(" + astor.to_source(node).strip().replace("\n", "") + ")"

    def extract_statements(body, prefix=""):
        for stmt in body:
            if isinstance(stmt, ast.If):
                condition = custom_unparse_condition(stmt.test)
                statements.append(f"{prefix}if {condition} {{")
                extract_statements(stmt.body, prefix=prefix + "    ")
                orelse = stmt.orelse
                while orelse:
                    first = orelse[0]
                    if isinstance(first, ast.If):
                        condition = custom_unparse_condition(first.test)
                        statements.append(f"{prefix}}} else if {condition} {{")
                        extract_statements(first.body, prefix=prefix + "    ")
                        orelse = first.orelse
                    else:
                        statements.append(f"{prefix}}} else {{")
                        extract_statements(orelse, prefix=prefix + "    ")
                        break
                statements.append(f'{prefix}}}')
            else:
                if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                    call = stmt.value
                    func_name = ""
                    if isinstance(call.func, ast.Attribute):
                        func_name = call.func.attr
                    elif isinstance(call.func, ast.Name):
                        func_name = call.func.id

                    if func_name == 'wait_until':
                        condition = custom_unparse_condition(call.args[0])
                        statements.append(f"{prefix}wait until{condition}")
                        continue

                line = astor.to_source(stmt).strip().replace("\n", "")
                statements.append(f"{prefix}{line}")

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_name = node.name

            result = {}
            statements = [""]
            result["name"] = class_name

            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                    for sub_item in item.body:
                        if isinstance(sub_item, ast.Assign):
                            target = sub_item.targets[0]
                            value = sub_item.value

                            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                                key = target.attr

                                if key in ["cron", "period"]:
                                    result[key] = ast.literal_eval(value)
                                else:
                                    raw_value = astor.to_source(value).strip().replace("\n", "")
                                    converted_value = replace_tags_arguments(raw_value)
                                    statements.append(f"{key} := {converted_value}")

                if isinstance(item, ast.FunctionDef) and item.name == "run":
                    extract_statements(item.body)

            code = '\n'.join(statements + [""])

            def replace_all_any_parentheses(text):
                result = ''
                i = 0
                while i < len(text):
                    if text[i:i+4] in ('All(', 'Any('):
                        func_name = text[i:i+3].lower()
                        i += 4
                        count = 1
                        start = i
                        while i < len(text) and count > 0:
                            if text[i] == '(':
                                count += 1
                            elif text[i] == ')':
                                count -= 1
                            i += 1
                        inner = text[start:i-1]
                        result += f'{func_name}{inner}'
                    else:
                        result += text[i]
                        i += 1
                return result

            code = replace_all_any_parentheses(replace_tags_arguments(code)).replace('self.', '').replace('wait_until', 'wait until')

            result["code"] = code.strip()
            result_total.append(result)

    return result_total


if __name__ == "__main__":
    example = "```python\nclass Scenario1:\n    def __init__(self):\n        self.cron = ''\n        self.period = -1\n\n    def run(self):\n        contact = Tags('ContactSensor').contactSensor_contact\n        alarm_state = Tags('Alarm').alarm_alarm\n\n        if contact == 'open' and alarm_state == 'off':\n            Tags('Alarm').alarm_siren()\n\nclass Scenario2:\n    def __init__(self):\n        self.cron = ''\n        self.period = -1\n\n    def run(self):\n        curtain_state = Tags('Curtain').curtain_curtain\n\n        if curtain_state == 'open':\n            Tags('Curtain').curtain_close()\n\nclass Scenario3:\n    def __init__(self):\n        self.cron = ''\n        self.period = -1\n\n    def run(self):\n        ac_state = Tags('AirConditioner').switch_switch\n        temperature = Tags('AirQualityDetector').temperatureMeasurement_temperature\n\n        if ac_state == 'off' and temperature >= 30.0:\n            Tags('AirConditioner').airConditionerMode_setAirConditionerMode('cool')\n            Tags('AirConditioner').switch_on()\n```"
    print(json.dumps(transform_code(example), indent=2, ensure_ascii=False).replace("\\n", "\n"))
