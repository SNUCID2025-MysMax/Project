import re,json,os, copy

import yaml
from yaml.representer import SafeRepresenter

class LiteralString(str):
    pass

def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

yaml.add_representer(LiteralString, literal_str_representer)

class QuotedString(str):
    pass

def quoted_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

yaml.add_representer(QuotedString, quoted_str_representer)

def parse_scenarios_with_command(script: str):
    lines = script.strip().splitlines()
    command = lines[0].replace("\",,","").replace("\"","")
    script = "\n".join(lines[1:]).strip()
    parts = [part.strip() for part in script.strip().split('---') if part.strip()]
    scenarios = []

    num = 1
    for part in parts:
        lines = part.strip().splitlines()
        name = lines[0].split('=', 1)[1].strip().strip('"')
        cron = lines[1].split('=', 1)[1].strip().strip('"')
        period = int(lines[2].split('=', 1)[1].strip())
        code = "\n".join(lines[3:]).strip() + "\n"  # 줄바꿈 포함시켜 | 출력 유도

        scenarios.append({
            # "name": QuotedString(name),
            "name": QuotedString(f'Scenario{num}'),
            "cron": QuotedString(cron),
            "period": period,
            "code": LiteralString(code)
        })
        num += 1

    return {
      "command": QuotedString(command),
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
            "name": QuotedString(name),
            "cron": QuotedString(cron),
            "period": period,
            "code": LiteralString(code)
        })

    return {
      "code": scenarios
    }

def extract_last_code_block(text):
    pattern = r"```(?:.*?\n)?(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches[-1] if matches else None

# yaml 속성을 LiteralString으로 변환
def print_yaml(file):
  with open(file, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    result = []
    for item in data:
      s = ""
      s += f"Generate SoP Lang code for \"{item['command']}\"\n```\n"
      sub = []
      for idx, i in enumerate(item['code']):
        if idx < 5:
            continue
        k = ""
        k += f"name = \"{i['name']}\"\n"
        k += f"cron = \"{i['cron']}\"\n"
        k += f"period = {i['period']}\n"
        k += i['code'].strip() + "\n"
        sub.append(k)
      s += "---\n".join(sub)
      s += "```\n"
      # print(item['code'][0]['code'].strip())
      result.append(s)
    return('\n'.join(result))


# for i in range(1,16):
#     filename = f"category_{i}"
#     with open(f"./Testset/Eval_gpt/evaluation_{filename}.yaml", "r") as f:
#         script = yaml.safe_load(f)
    
    
#     for item in script:
#         gen = item["generated_code"]

#         try:
#             code = parse_scenarios(extract_last_code_block(gen))['code']
#         except:
#             try:
#                 code = parse_scenarios(gen)['code']
#             except:
#                 print("failed")
#                 code = [{'name': 'Scenario1', 'cron': '', 'period': -1, 'code': '(#AirConditioner).switch_on()\n'}]
#         item["transformed_code"] = code

#         label = item["label"]

#         label_for_yaml = copy.deepcopy(label)
#         for l in label_for_yaml:
#             l["code"] = LiteralString(l["code"])

#         code_for_yaml = copy.deepcopy(code)
#         for c in code_for_yaml:
#             c["code"] = LiteralString(c["code"])

#         item["label"] = label_for_yaml
#         item["generated_code"] = LiteralString(item["generated_code"])
#         item["transformed_code"] = code_for_yaml

#     with open(f"./Testset/Eval_gpt/evaluation_{filename}.yaml", "w", encoding="utf-8") as out_file:
#         yaml.dump(script, out_file, indent=2, allow_unicode=True, sort_keys=False, width=float('inf'))
