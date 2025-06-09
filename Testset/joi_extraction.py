import re,json,os

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


with open("./test.txt", "r", encoding="utf-8") as f:
    dsl_codes = f.read()

# # print(json.dumps(parse_scenarios(dsl_code), indent=2))
with open("./test.yaml", "w", encoding="utf-8") as f:
    yaml.dump([parse_scenarios(dsl_codes)], f, indent=2, allow_unicode=True, sort_keys=False, width=float('inf'))
    # yaml.dump([parse_scenarios_with_command(dsl_code.strip()) for dsl_code in dsl_codes.split("------")],
    #            f, indent=2, allow_unicode=True, sort_keys=False, width=float('inf'))

# --------------------------------------------------------------------------------------#
# yaml 속성을 LiteralString으로 변환
def print_yaml(file):
  with open(file, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    result = []
    for item in data:
      s = ""
      s += item['command'] + "\n"
      sub = []
      for i in item['code']:
        k = ""
        k += f"name = \"{i['name']}\"\n"
        k += f"cron = \"{i['cron']}\"\n"
        k += f"period = {i['period']}\n"
        k += i['code'].strip() + "\n"
        sub.append(k)
      s += "---\n".join(sub)
      # print(item['code'][0]['code'].strip())
      result.append(s)
    print('\n'.join(result))
#print_yaml("./Testset/category_13.yaml")

# --------------------------------------------------------------------------------------#

# # 줄바꿈 변환
# def process_fields(data, quote_fields, literal_fields):
#     if isinstance(data, list):
#         for item in data:
#             process_fields(item, quote_fields, literal_fields)
#     elif isinstance(data, dict):
#         for key, value in data.items():
#             if key in quote_fields and isinstance(value, str):
#                 # 줄바꿈 제거 및 큰따옴표로 감싸기
#                 single_line = re.sub(r'\s*\n\s*', ' ', value).strip()
#                 data[key] = QuotedString(single_line)
#             elif key in literal_fields and isinstance(value, str):
#                 # LiteralString으로 변환
#                 data[key] = LiteralString(value)
#             else:
#                 process_fields(value, quote_fields, literal_fields)


# for file in os.listdir("./Testset"):
#   if file.endswith("yaml"):
#     with open(f"./Testset/{file}", "r", encoding="utf-8") as f:
#       yaml_data = yaml.safe_load(f)
#     process_fields(yaml_data, quote_fields=["command", "name", "cron"], literal_fields=["code"])
#     with open(f"./Testset/{file}", "w", encoding="utf-8") as f:
#       yaml.dump(yaml_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False, width=float('inf'))

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

