import os
import re
import json
import glob
import importlib.util
from tqdm import tqdm

# 🔁 바꿀 단어 설정
WORD_FROM = "공급합니다."
WORD_TO = "공급해줘."


# 변수 로드 함수
def load_variable_from_pyfile(filepath, var_name):
    spec = importlib.util.spec_from_file_location("module.name", filepath)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return getattr(foo, var_name)

# 단어 치환 함수
def replace_words(input_data):
    for dialogue in input_data:
        for msg in dialogue:
            if msg["from"] == "human":
                match = re.search(r"Input: (.*?)\n\nServices:", msg["value"], re.DOTALL)
                if match:
                    original_text = match.group(1).strip()
                    if WORD_FROM in original_text:
                        replaced_text = original_text.replace(WORD_FROM, WORD_TO)
                        print(f"🔁 치환: {original_text} → {replaced_text}")
                        msg["value"] = msg["value"].replace(original_text, replaced_text)
    return input_data

# 경로 설정
file_path = "./finetune_KO/data_total.py"
var_name = "data_total"

try:
    print(f"\n📄 파일 처리 시작: {file_path}")
    data = load_variable_from_pyfile(file_path, var_name)
    updated_data = replace_words(data)

    # 저장
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"{var_name} = {json.dumps(updated_data, ensure_ascii=False, indent=4)}\n")
    print(f"✅ 저장 완료: {file_path}")
except Exception as e:
    print(f"❌ 오류 발생: {file_path} - {e}")