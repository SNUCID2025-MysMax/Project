import json, os
from conversion import transform_code

# with open("./category0.json", "r", encoding="utf-8") as f:
    
#     data = json.load(f)
#     result = []

#     for item in data:
#         c = item["python"]
#         c = "class Scenario1:\n    def __init__(self):\n        self.cron = \"\"\n        self.period = -1\n\n    def run(self):\n        " + c.replace("\n   ","\n            ")
#         c = "```python\n" + c + "\n```"

#         result.append({
#             "command": item["command"],
#             "python": c,
#             "code": transform_code(c),
#         })


#     with open("./category_0.json", "w", encoding="utf-8") as f:
#         json.dump(result, f, indent=2, ensure_ascii=False)

# file = "category_4.json"
# with open(f"./Testset/{file}", "r", encoding="utf-8") as f:
    
#     data = json.load(f)
#     result = []

#     for item in data:
#         c = item["python"]
#         # c = "class Scenario1:\n    def __init__(self):\n        self.cron = \"\"\n        self.period = -1\n\n    def run(self):\n        " + c.replace("\n   ","\n            ")
#         c = "```python\n" + c + "\n```"

#         result.append({
#             "command": item["command"],
#             "python": c,
#             "code": transform_code(c),
#         })


#     with open(f"./Testset/{file}", "w", encoding="utf-8") as f:
#         json.dump(result, f, indent=2, ensure_ascii=False)



def print_json_pretty_with_real_newlines(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ 입력 파일 읽는 중 오류 발생: {e}")
        return

    try:
        json_str = json.dumps(data, indent=4, ensure_ascii=False)
        # json.dumps는 문자열 내 줄바꿈을 \\n으로 만듦 → \n으로 복원
        json_str = json_str.replace('\\n', '\n')

        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.write(json_str)
    except Exception as e:
        print(f"❌ 출력 파일 저장 중 오류 발생: {e}")


for file in os.listdir("./Testset"):
    if file.endswith(".json"):
        try:
            with open(f"./Testset/{file}", "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ {file} 읽는 중 오류 발생: {e}")
            continue

        result = []

        for item in data:
            result.append({
                "command": item["command"],
                "python": item["python"],
                "code": transform_code(item["python"]),
            })

        try:
            with open(f"./Testset/{file}", "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"✅ {file} 처리 완료")
        except Exception as e:
            print(f"❌ {file} 저장 중 오류 발생: {e}")

        input_path = f"./Testset/{file}"
        output_path = f"./Testset/{file[:-5]}.txt"
        print_json_pretty_with_real_newlines(input_path, output_path)


