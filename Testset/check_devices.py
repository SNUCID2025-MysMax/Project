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

test_dir = "./TestsetWithDevices_translated"
generated_dir = "./Eval_qwenCoder"

for i in range(0, 17):
    file_name = f"{test_dir}/category_{i}.yaml"
    generated_name = f"{generated_dir}/evaluation_category_{i}.yaml"
    print(f"Processing file: {file_name}")

    with open(file_name, "r") as f:
        data = yaml.safe_load(f)
    
    with open(generated_name, "r") as f:
        generated_data = yaml.safe_load(f)

    # 각 항목에 devices 키 추가
    for idx, item in enumerate(data):
        generated_item = generated_data[idx]
        # print(generated_item["devices"])
        for code in item["code"]:
            text = code["code"]
            matches = re.findall(r"#([A-Za-z0-9]+)(?=[^A-Za-z0-9])", text)
            matches = {m for m in matches if m not in exclude}
        ret = []
        for match in matches:
            if match not in generated_item["devices"]:
                ret.append(match)
        print(ret)

#############################################33
# import re

# for i in range(0,16):
#     file_name = f"category_{i}.yaml"
#     print(f"Processing file: {file_name}")
#     path_out = f"./Testset/TestsetWithDevices/{file_name}"

#     with open(path_out, "r") as f:
#         data = yaml.safe_load(f)

#     # 각 항목에 devices 키 추가
#     for item in tqdm.tqdm(data):
#         command = item["command"]
#         devices = item["devices"]

#         empty = []
#         for code in item["code"]:
#             text = code["code"]
#             matches = re.findall(r"#([A-Za-z0-9]+)(?=[^A-Za-z0-9])", text)

#             for match in matches:
                
#                 if match not in devices and match not in exclude:
#                     empty.append(match)
#         if empty != []:
#             print(i, command, empty)
