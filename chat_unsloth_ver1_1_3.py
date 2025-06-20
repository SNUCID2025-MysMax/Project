import os, sys, re, gc, yaml, time, json, copy, requests
from datetime import datetime

from tqdm import tqdm

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString
from ruamel.yaml.scalarstring import DoubleQuotedScalarString

yaml = YAML()
yaml.default_flow_style = False
yaml.allow_unicode = True
yaml.width = float('inf')

# from Evaluation.compare_soplang_ir import  compare_codes
from Evaluation.compare_soplang_ir import   compare_all
from Evaluation.compare_custom import  compare_all_print

with open("./Demo/things.json", "r") as f:
    things = json.load(f)

with open("./Demo/things_extra_tags.json", "r") as f:
    things_tags = json.load(f)

def main():
    # model_name = "GPT"
    model_name = "qwenCoder"
    connected_devices = things
    lst = list(range(0,12))+[13]
    for i in lst:
        if (i == 13 or i == 15):
            connected_devices = things_tags
        print(f"Processing category {i}...")
        with open(f"./Testset/TestsetWithDevices_translated_no_seperation/category_{i}.yaml", "r") as f:
            results = []
            data = yaml.load(f)

            for idx, item in tqdm(enumerate(data)):
                # if idx >= 5:
                #     continue
                user_command = item["command_translated"]
                user_command_origin = item["command"]

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                payload = {
                    "sentence": user_command,
                    "model": model_name,
                    "connected_devices": connected_devices,
                    "current_time": current_time,
                    "other_params": [],
                }

                resp = requests.post("http://localhost:8000/generate_joi_code", json=payload)

                codes = resp.json().get("code", [])
                code_lst = []
                for code in codes:
                    code_dict = {}
                    code_dict["name"] = DoubleQuotedScalarString(code["name"])
                    code_dict["cron"] = DoubleQuotedScalarString(code["cron"])
                    code_dict["period"] = code["period"]
                    raw_code = code["code"].strip().replace('\\n', '\n').replace('\\"', '"').replace("\\'", '"').replace("'", '"')
                    code_dict["code"] = LiteralScalarString(raw_code+'\n')
                    code_lst.append(code_dict)
                service_selected = resp.json()["log"]["mapped_devices"]
                command_translated = resp.json()["log"]["translated_sentence"]
                response_time = resp.json()["log"]["response_time"]

                entry = {
                    "command": DoubleQuotedScalarString(user_command_origin),
                    "command_translated": DoubleQuotedScalarString(command_translated),
                    "devices": list(service_selected),
                    "generated_code": code_lst,
                    "elapsed_time": response_time,
                }
                results.append(entry)

        if (i == 13 or i == 15):
            connected_devices = things

        os.makedirs(f"./Testset/Eval_{model_name}_250621/", exist_ok=True)
        with open(f"./Testset/Eval_{model_name}_250621/evaluation_category_{i}.yaml", "w", encoding="utf-8") as out_file:
            yaml.dump(results, out_file)

    gc.collect()

if __name__ == "__main__":
    # main()
    # compare_all("qwenCoder_250616")
    # compare_all("GPT_250618")
    # compare_all_print("qwenCoder_250619_english")
    # compare_all_print("qwenCoder_250618_korean")
    # compare_all_print("GPT_250618")
    compare_all_print("qwenCoder_250621")
