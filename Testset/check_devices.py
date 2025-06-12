
import os, sys, tqdm, re
import yaml
from yaml.representer import SafeRepresenter

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString
from ruamel.yaml.scalarstring import DoubleQuotedScalarString

yaml = YAML()
yaml.default_flow_style = False
yaml.allow_unicode = True
yaml.width = float('inf')

# test_dir = "./TestsetWithDevices_translated"
# output_dir = "./TestsetWithDevices_translated2"
# for i in range(0, 17):
#     file_name = f"{test_dir}/category_{i}.yaml"
#     output_name = f"{output_dir}/category_{i}.yaml"

#     ret = []

#     with open(file_name, "r") as f:
#         data = yaml.load(f)

#     print(file_name)
#     for idx,item in enumerate(data):
#         ret_dict = {}
#         ret_dict["command"] = DoubleQuotedScalarString(item["command"])
#         ret_dict["command_translated"] = DoubleQuotedScalarString(item["command_translated"])
#         code_lst = []
#         for code in item["code"]:
#             code_dict = {}
#             code_dict["name"] = DoubleQuotedScalarString(code["name"])
#             code_dict["cron"] = DoubleQuotedScalarString(code["cron"])
#             code_dict["period"] = code["period"]
#             raw_code = code["code"].strip().replace('\\n', '\n').replace('\\"', '"').replace("\\'", '"').replace("'", '"')
#             code_dict["code"] = LiteralScalarString(raw_code+'\n')
#             code_lst.append(code_dict)
#         ret_dict["code"] = code_lst
#         ret_dict["devices"] = item["devices"]
#         ret.append(ret_dict)
#     with open(output_name, "w") as f:
#         yaml.dump(ret, f)


exclude = {"Wall", "SectorA", "SectorB", "Upper", "Lower", "Even", "Odd"}

test_dir = "./TestsetWithDevices_translated"
generated_dir = "./Eval_qwenCoder"

for i in range(0, 17):
    file_name = f"{test_dir}/category_{i}.yaml"
    generated_name = f"{generated_dir}/evaluation_category_{i}.yaml"
    print(f"Processing file: {file_name}")

    with open(file_name, "r") as f:
        data = yaml.load(f)
    
    with open(generated_name, "r") as f:
        generated_data = yaml.load(f)

    for idx, item in enumerate(data):
        generated_item = generated_data[idx]
        
        for code in item["code"]:
            text = code["code"]
            matches = re.findall(r"#([A-Za-z0-9]+)(?=[^A-Za-z0-9])", text)
            matches = {m for m in matches if m not in exclude}
        ret = []
        for match in matches:
            if match not in generated_item["devices"]:
                ret.append(match)
        if ret:
            print(generated_item["command"], ret)

#############################################33
# import re

# for i in range(0,16):
#     file_name = f"category_{i}.yaml"
#     print(f"Processing file: {file_name}")
#     path_out = f"./Testset/TestsetWithDevices/{file_name}"

#     with open(path_out, "r") as f:
#         data = yaml.load(f)

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
