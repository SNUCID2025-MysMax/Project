import json
from conversion import transform_code

# with open("/home/endermaru/Project/Testset/category0.json", "r", encoding="utf-8") as f:
    
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


#     with open("/home/endermaru/Project/Testset/category_0.json", "w", encoding="utf-8") as f:
#         json.dump(result, f, indent=2, ensure_ascii=False)


# for i in range(12):
file = f"category_5.json"
with open(f"/home/endermaru/Project/Testset/{file}", "r", encoding="utf-8") as f:
    data = json.load(f)
    result = []

    for item in data:
        print(item['command'])
        print(item["python"])
        result.append({
            "command": item["command"],
            "python": item["python"],
            "code": transform_code(item["python"]),
        })

    # print(result)

    with open(f"/home/endermaru/Project/Testset/{file}", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
