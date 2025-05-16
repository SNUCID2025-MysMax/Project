import re,json,os

import yaml
from yaml.representer import SafeRepresenter

class LiteralString(str):
    pass

def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

yaml.add_representer(LiteralString, literal_str_representer)

def parse_scenarios_with_command(script: str):
    lines = script.strip().splitlines()
    command = lines[0].replace("\",,","").replace("\"","")
    script = "\n".join(lines[1:]).strip()
    parts = [part.strip() for part in script.strip().split('---') if part.strip()]
    scenarios = []

    for part in parts:
        lines = part.strip().splitlines()
        name = lines[0].split('=', 1)[1].strip().strip('"')
        cron = lines[1].split('=', 1)[1].strip().strip('"')
        period = int(lines[2].split('=', 1)[1].strip())
        code = "\n".join(lines[3:]).strip() + "\n"  # 줄바꿈 포함시켜 | 출력 유도

        scenarios.append({
            "name": name,
            "cron": cron,
            "period": period,
            "code": LiteralString(code)
        })

    return {
      "command": command,
      "code": scenarios
      }

def parse_scenarios(script: str):
    parts = [part.strip() for part in script.strip().split('---') if part.strip()]
    scenarios = []

    for part in parts:
        lines = part.strip().splitlines()
        name = lines[0].split('=', 1)[1].strip().strip('"')
        cron = lines[1].split('=', 1)[1].strip().strip('"')
        period = int(lines[2].split('=', 1)[1].strip())
        code = "\n".join(lines[3:]).strip() + "\n"  # 줄바꿈 포함시켜 | 출력 유도

        scenarios.append({
            "name": name,
            "cron": cron,
            "period": period,
            "code": LiteralString(code)
        })

    return {
      "code": scenarios
    }

dsl_code = '''
에어컨이 지원하는 모드를 스피커로 출력해줘
name = "Scenario1"
cron = ""
period = -1
modes_str = (#AirConditioner).airConditionerMode_supportedAcModes
(#Speaker).mediaPlayback_speak(modes_str)
'''

# print(json.dumps(parse_scenarios(dsl_code), indent=2))
with open("./test.yaml", "w", encoding="utf-8") as f:
    yaml.dump([parse_scenarios_with_command(dsl_code)], f, indent=2, allow_unicode=True, sort_keys=False)
# print(yaml.dump(parse_scenarios(dsl_code), indent=2, allow_unicode=True, sort_keys=False))

# # 예전 json을 yaml로 변환
# def adjust_indentation(code_str, from_spaces=4, to_spaces=2):
#     lines = code_str.splitlines()
#     adjusted_lines = [
#         line.replace(' ' * from_spaces, ' ' * to_spaces, 1) if line.startswith(' ' * from_spaces) else line
#         for line in lines
#     ]
#     return '\n'.join(adjusted_lines)

# for file in os.listdir("./Testset"):
#   if file.endswith(".json"):
#     try:
#       with open(f"./Testset/{file}", "r", encoding="utf-8") as f:
#         data = json.load(f)
#     except Exception as e:
#       print(f"❌ {file} 읽는 중 오류 발생: {e}")
#       continue

#     result = []

#     for item in data:
#       result.append({
#         "command": item["command"],
#         "code": [
#           {
#             "name": i["name"],
#             "cron": i["cron"],
#             "period": i["period"],
#             "code": LiteralString(adjust_indentation(i["code"]))
#           }
#           for i in item["code"]
#         ]
#       })
#     with open(f"./Testset/{file[:-5]}.yaml", "w", encoding="utf-8") as f:
#       yaml.dump(result, f, indent=2, allow_unicode=True, sort_keys=False)


