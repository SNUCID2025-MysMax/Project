import os
import json
import requests
import re
import importlib.util
import glob
from tqdm import tqdm
import time

# ✅ Deepl 번역 함수 (Google 번역 → Deepl로 교체)
def deepl_translate(command, auth_key="6bc9c430-2abd-4f64-9f0d-09f6ac92441f:fx"):
    url = "https://api-free.deepl.com/v2/translate"
    data = {
        "auth_key": auth_key,
        "text": command,
        "source_lang": "EN",
        "target_lang": "KO"
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

def load_variable_from_pyfile(filepath, var_name):
    spec = importlib.util.spec_from_file_location("module.name", filepath)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return getattr(foo, var_name)

def translate_and_save(input_data, output_path, var_name):
    changed = False
    for i, dialogue in enumerate(tqdm(input_data, desc="🔄 전체 대화 번역 중")):
        for j, msg in enumerate(dialogue):
            if msg["from"] == "human":
                match = re.search(r"Input: (.*?)\n\nServices:", msg["value"], re.DOTALL)
                if match:
                    english_input = match.group(1).strip()
                    if re.search(r'[a-zA-Z]', english_input):  # 영어가 있는 경우만 번역
                        print(f"🌐 번역 중: {english_input}")
                        korean_translation = deepl_translate(english_input)
                        print(f"✅ 결과: {korean_translation}")
                        msg["value"] = msg["value"].replace(english_input, korean_translation)
                        changed = True

                        # 🔐 중간 저장
                        with open(output_path, "w", encoding="utf-8") as f:
                            f.write(f"{var_name} = {json.dumps(input_data, ensure_ascii=False, indent=4)}\n")
                        time.sleep(1)
    return input_data

# 경로 설정
input_dir = "./finetune"
output_dir = "./finetune_KO"
os.makedirs(output_dir, exist_ok=True)

# data_*.py 파일들만 처리
for filepath in glob.glob(os.path.join(input_dir, "data_*.py")):
    filename = os.path.basename(filepath)
    var_name = filename.replace(".py", "")
    output_path = os.path.join(output_dir, filename)

    try:
        print(f"\n📄 파일 처리 시작: {filename}")
        data = load_variable_from_pyfile(filepath, var_name)
        translate_and_save(data, output_path, var_name)
        print(f"✅ 저장 완료: {output_path}")
    except Exception as e:
        print(f"❌ 오류 발생: {filename} - {e}")
