import unittest
import json
from soplang_parser_full import parser, lexer
from compare_soplang_ir import parse_script_json, compare_codes, extract_logic_expressions
from soplang_ir_simulator import generate_context_from_conditions, flatten_actions

'''
class TestSoplangParserFull(unittest.TestCase):

    def test_basic(self):
        json_data = {
            "name": "",
            "cron": "* * * * *",
            "period": 1000,
            "script": "if(temperature > 30) {\\n  (#fan).on()\\n}"
        }
        tree = parse_script_json(json_data)
        print("\n[basic AST]:\n", json.dumps(tree, indent=2))
        self.assertIsInstance(tree, dict)

    def test_cron(self):
        json_data = {
            "name": "사무실 움직임 시 불 켜고 사진 전송",
            "cron": "* * * * *",
            "period": 1000,
            "script": "if ((#office #movement).detected == 1 && (#office).brightness < 50) {\\n  (#office #light).turn_on()\\n  x = (#office).take_picture()\\n  (#util).send_mail(\"움직임 감지\", x)\\n}"
        }
        tree = parse_script_json(json_data)
        print("\n[cron AST]:\n", json.dumps(tree, indent=2))
        self.assertIsNotNone(tree, dict)
    
    def test_functioncall(self):
        json_data = {
            "name": "",
            "cron": "* * * * *",
            "period": 1000,
            "script": "photo = (#Camera).take()"
        }
        tree = parse_script_json(json_data)
        print("\n[function_call AST]:\n", json.dumps(tree, indent=2))
        self.assertIsNotNone(tree, dict)
    
    def test_all(self):
        json_data = {
            "name": "",
            "cron": "* * * * *",
            "period": 1000,
            "script": "all(#Light).off()"
        }
        tree = parse_script_json(json_data)
        print("\n[all AST]:\n", json.dumps(tree, indent=2))
        self.assertIsNotNone(tree, dict)
        
    def test_arithmetic_expression(self):
        json_data = {
            "name": "산술 연산 테스트",
            "cron": "* * * * *",
            "period": 1000,
            "script": "x := 4 / 3\\ny = x + 2\\n(#target).set_temp(y)"
        }
        tree = parse_script_json(json_data)
        print("\n[산술 연산 AST]:\n", json.dumps(tree, indent=2))
        self.assertIsNotNone(tree)
        self.assertIsInstance(tree, dict)
    def test_delay_statement(self):
        json_data = {
            "name": "지연 테스트",
            "cron": "* * * * *",
            "period": 1000,
            "script": "delay(1000)\\n(#speaker).say(\"1초 경과\")"
        }
        tree = parse_script_json(json_data)
        print("\n[Delay AST]:\n", json.dumps(tree, indent=2))
        self.assertIsNotNone(tree)
        self.assertIsInstance(tree, dict)

class TestCompareSoplangIR(unittest.TestCase):

    def test_compare_equivalent_scripts(self):
        gold = {
            "name": "기준 스크립트",
            "cron": "* * * * *",
            "period": 1000,
            "script": "x := 4 / 3\\ny = x + 2\\n(#target).set_temp(y)"
        }
        pred = {
            "name": "유사 스크립트",
            "cron": "* * * * *",
            "period": 1000,
            "script": "x := 4 / 3\\ny = x + 2\\n(#target).set_temp(y)"
        }

        result = compare_codes(gold, pred)
        print("\n✅ [compare_equivalent_scripts result]:\n", json.dumps(result, indent=2))
        self.assertTrue(result["cron_equal"])
        self.assertTrue(result["period_equal"])
        self.assertTrue(result["logic_equivalent"])
        self.assertEqual(result["script_similarity"], 1.0)

    def test_compare_different_logic(self):
        gold = {
            "name": "문턱값 높음",
            "cron": "* * * * *",
            "period": 1000,
            "script": "if (temperature > 30) {\\n  (#fan).on()\\n}"
        }
        pred = {
            "name": "문턱값 낮음",
            "cron": "* * * * *",
            "period": 1000,
            "script": "if (temperature > 10) {\\n  (#fan).on()\\n}"
        }

        result = compare_codes(gold, pred)
        print("\n❗ [compare_different_logic result]:\n", json.dumps(result, indent=2))
        self.assertTrue(result["cron_equal"])
        self.assertTrue(result["period_equal"])
        self.assertFalse(result["logic_equivalent"])
        self.assertLess(result["script_similarity"], 1.0)
'''
def parse_script_only(script_code: str):
    wrapped_code = f"{{\n{script_code}\n}}"
    return parser.parse(wrapped_code, lexer=lexer)

class TestSoplangIrSimulator(unittest.TestCase):
    def test_condition_contexts_and_actions(self):
        script = '''
        if ((#sensor).temp > 30 or (#sensor).humidity < 50) {
            (#fan).on()
        }
        '''

        ast = parse_script_only(script)
        logic = extract_logic_expressions(ast)

        print("\n[Extracted Logic Conditions]:")
        for l in logic:
            print(json.dumps(l, indent=2))

        contexts = generate_context_from_conditions(logic)

        print(f"\n[Generated Contexts] ({len(contexts)} variants):")
        for ctx in contexts:
            print(ctx)

        print("\n[Actions for each context]:")
        for i, ctx in enumerate(contexts):
            actions = flatten_actions(ast, context=ctx.copy())
            print(f"\nContext #{i+1}: {ctx}")

            action_only = [a for a in actions if a[0] == "Action"]
            if not action_only:
                print("  ⚠️ No actions executed")
            else:
                for act in action_only:
                    target = act[1]
                    service = act[2]
                    args = ", ".join(map(str, act[3])) if act[3] else ""
                    print(f"  → Action: {target}.{service}({args})")

if __name__ == '__main__':
    unittest.main()
