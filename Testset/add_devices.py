import os, sys, tqdm, re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from FlagEmbedding import BGEM3FlagModel
# from Embedding.embedding import hybrid_recommend

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

yaml.SafeDumper.add_representer(LiteralString, literal_str_representer)
yaml.SafeDumper.add_representer(QuotedString, quoted_str_representer)


exclude = {"Wall", "SectorA", "SectorB", "Upper", "Lower", "Even", "Odd"}

# model_dir = os.path.expanduser("./models/bge-m3")
# model_bge = BGEM3FlagModel(model_dir, use_fp16=False, local_files_only=True)
# hybrid_recommend(model_bge, "에어컨", max_k=7)
# print("Embedding loaded")



# for i in range(0,16):
#     file_name = f"category_{i}.yaml"
#     print(f"Processing file: {file_name}")
#     path_in = f"./Testset/Testset/{file_name}"
#     path_out = f"./Testset/TestsetWithDevices/{file_name}"

#     with open(path_in, "r") as f:
#         data = yaml.safe_load(f)

#     # 각 항목에 devices 키 추가
#     for item in tqdm.tqdm(data):
#         user_command = item["command"]

#         result = set()

#         for code in item["code"]:
#             code["code"] = LiteralString(code["code"])

#             text = code["code"]
#             matches = re.findall(r"#([A-Za-z0-9]+)(?=[^A-Za-z0-9])", text)
#             matches = {m for m in matches if m not in exclude}
#             result.update(matches)
        
#         item["devices"] = list(result)



#         # 만약 첫 번째 항목만 처리 후 멈추려면 이 줄을 유지하세요
#         # break


#     # 변경된 데이터 YAML로 저장
#     with open(path_out, "w") as f:
#         yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False,  width=float('inf'), default_flow_style=False)

#############################################33
import re

for i in range(0,16):
    file_name = f"category_{i}.yaml"
    print(f"Processing file: {file_name}")
    path_out = f"./Testset/TestsetWithDevices/{file_name}"

    with open(path_out, "r") as f:
        data = yaml.safe_load(f)

    # 각 항목에 devices 키 추가
    for item in tqdm.tqdm(data):
        command = item["command"]
        devices = item["devices"]

        empty = []
        for code in item["code"]:
            text = code["code"]
            matches = re.findall(r"#([A-Za-z0-9]+)(?=[^A-Za-z0-9])", text)

            for match in matches:
                
                if match not in devices and match not in exclude:
                    empty.append(match)
        if empty != []:
            print(i, command, empty)
