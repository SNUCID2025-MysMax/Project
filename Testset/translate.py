import os
import json
import requests
import re
import importlib.util
import glob
from tqdm import tqdm
import time
from collections import OrderedDict

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

def represent_ordereddict(dumper, data):
    return dumper.represent_dict(data.items())

yaml.SafeDumper.add_representer(OrderedDict, represent_ordereddict)
yaml.SafeDumper.add_representer(LiteralString, literal_str_representer)
yaml.SafeDumper.add_representer(QuotedString, quoted_str_representer)


# ✅ Deepl 번역 함수 (Google 번역 → Deepl로 교체)
def deepl_translate(command, auth_key="6bc9c430-2abd-4f64-9f0d-09f6ac92441f:fx"):
    url = "https://api-free.deepl.com/v2/translate"
    data = {
        "auth_key": auth_key,
        "text": command,
        "source_lang": "KO",
        "target_lang": "EN"
    }

    try:
        response = requests.post(url, data=data, timeout=10)
        if response.status_code == 200:
            return response.json()['translations'][0]['text']
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"⚠️ 번역 실패: \"{command}\" → {e}")
        return command  # 실패 시 원문 유지

def translate_quoted_strings(code_str):
    # 큰따옴표로 둘러싸인 문자열 추출
    def replace_func(match):
        original = match.group(0)  # "문자열"
        inner = original[1:-1]     # 문자열
        translated = deepl_translate(inner)
        return f'"{translated}"'

    return re.sub(r'"([^"\\]*(\\.[^"\\]*)*)"', replace_func, code_str)

# # 경로 설정
# input_dir = "./TestsetWithDevices"
# output_dir = "./TestsetWithDevices_translated"
# os.makedirs(output_dir, exist_ok=True)

# for f in os.listdir(input_dir):
#     if not f.endswith("16.yaml"):
#         continue
#     data = yaml.safe_load(open(os.path.join(input_dir, f), "r", encoding="utf-8"))
#     for item in data:
#         print(item["code"])
#         item["command_translated"] = deepl_translate(item["command"])
#         time.sleep(0.3)

#         for code in item["code"]:
#             code["code"] = translate_quoted_strings(code["code"])
#             code["code"] = LiteralString(code["code"])
#         # print(f"Processing: {item['command']}")

#     with open(os.path.join(output_dir, f), "w", encoding="utf-8") as f:
#         yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False,  width=float('inf'), default_flow_style=False)

# 경로 설정
origin_dir = "./TestsetWithDevices"
input_dir = "./TestsetWithDevices"
output_dir = "./TestsetWithDevices_translated"
os.makedirs(output_dir, exist_ok=True)

for f in os.listdir(input_dir):
    if not f.endswith("16.yaml"):
        continue
    # data_origin = yaml.safe_load(open(os.path.join(origin_dir, f), "r", encoding="utf-8"))
    data = yaml.safe_load(open(os.path.join(input_dir, f), "r", encoding="utf-8"))
    ret = []
    for idx, item in enumerate(data):
        el = OrderedDict()
        el["command"] = item["command"]
        el["command_translated"] = deepl_translate(item["command"])
        time.sleep(0.3)
        for code in item["code"]:
            code["code"] = translate_quoted_strings(code["code"])
            code["code"] = LiteralString(code["code"])
        el["code"] = item["code"]
        time.sleep(0.3)
        el["devices"] = item["devices"]
        # print(f"Processing: {item['command']}")
        ret.append(el)

    with open(os.path.join(output_dir, f), "w", encoding="utf-8") as f:
        yaml.safe_dump(ret, f, allow_unicode=True, sort_keys=False,  width=float('inf'), default_flow_style=False)