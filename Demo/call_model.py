import pandas as pd
import json, ast, requests, time
from datetime import datetime
from tqdm import tqdm
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Evaluation.compare_soplang_ir import compare_codes

with open("things.json", "r") as f:
    things = json.load(f)
# print(things)

model = "Qwen2.5-Coder:7B"
model = "gpt-4.1-mini"
is_english = False
if is_english:
    english = "_english"
else:
    english = ""

# df = pd.read_excel("./final_output_250616.xlsx", engine='openpyxl')
df = pd.read_csv("./final_output_250616.csv", encoding='utf-8-sig')

if f"joi{english}_pred_{model}" not in df.columns:
    df[f"joi_pred{english}_{model}"] = ""
    df[f"cloud_similarity{english}_{model}"] = 0.0
    df[f"script_similarity{english}_{model}"] = 0.0
    df[f"response_time{english}_{model}"] = ""

output_path = "./final_output_250616.csv"

for i, row in tqdm(df.iterrows()):
    if row.get("selected") != 1:
        continue
    # if i<306:
    #     continue

    print(f"Processing row {i+1}/{len(df)}: {row['command']}")

    sentence = row[f"command{english}"]
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    connected_devices = row["connected_dievces"]
    other_params = row["options"]

    # 파싱
    if pd.isna(other_params):
        other_params = []
    else:
        try:
            other_params = ast.literal_eval(other_params)
        except:
            other_params = []

    if isinstance(connected_devices, str) and not pd.isna(connected_devices) and connected_devices.strip():
        try:
            connected_devices = ast.literal_eval(connected_devices)
        except:
            connected_devices = things
    else:
        connected_devices = things

    payload = {
        "sentence": sentence,
        "model": model,
        "connected_devices": connected_devices,
        "current_time": current_time,
        "other_params": other_params,
    }

    start = time.time()
    resp = requests.post("http://localhost:8000/generate_joi_code", json=payload)
    end = time.time()
    try:
        generated_code = (resp.json().get("code", ""))
    except:
        generated_code = []
    # generated_code = (resp.json().get("code", ""))
    # print(generated_code)
    resp_time = f"{end - start:.3f}"

    # gt = ast.literal_eval(row["joi_gt"])

    # eval = compare_codes(gt, generated_code)
    # total_score = eval["ast_similarity"]
    # if eval["cron_eqaul"]:
    #     total_score *= 0.5
    # if eval["period_eqaul"]:
    #     total_score *= 0.5
    
    df.at[i, f"joi_pred{english}_{model}"] = str(generated_code)
    df.at[i, f"cloud_similarity{english}_{model}"] = 0.0
    df.at[i, f"script_similarity{english}_{model}"] = 0.0
    df.at[i, f"response_time{english}_{model}"] = resp_time

    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    # break