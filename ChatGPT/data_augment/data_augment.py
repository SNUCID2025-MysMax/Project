from openai import OpenAI
from dotenv import load_dotenv
import ast
import os
from datetime import datetime
import json
import re
import sys
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from grammar import grammar
from conversion import transform_code
import glob

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

#print("🔍 Loaded API Key:", api_key)
client = OpenAI(api_key=api_key)

def load_prompt_roles(path, **kwargs):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    
    messages = []
    parts = re.split(r"###\s*(system|user|assistant)", raw)
    for i in range(1, len(parts), 2):
        role = parts[i].strip()
        content = parts[i+1].strip().format(**kwargs)
        messages.append({"role": role, "content": content})
    
    return messages

    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

# ===  Device 클래스 및 기능 추출 === #
def extract_device_skills(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    device_skills = {}

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            for stmt in node.body:
                if isinstance(stmt, ast.Assign):
                    for target in stmt.targets:
                        if isinstance(target, ast.Name) and target.id == 'skills':
                            skills = []
                            if isinstance(stmt.value, (ast.Set, ast.List)):
                                for elt in stmt.value.elts:
                                    if isinstance(elt, ast.Attribute):
                                        skills.append(elt.attr)
                            if skills:
                                device_skills[class_name] = skills
    return device_skills

def parse_class_docstrings(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = r'class\s+(\w+)\s*:\s*"""(.*?)"""'
    matches = re.finditer(pattern, text, re.DOTALL)

    class_dict = {}
    for match in matches:
        class_name = match.group(1)
        class_body = match.group(0)
        class_dict[class_name] = class_body.strip()

    return class_dict

def sample_device_classes(class_dict, k=3):
    selected_keys = random.sample(list(class_dict.keys()), k)
    return "\n\n".join(class_dict[k] for k in selected_keys)

import re
from datetime import datetime

def process_refined_commands(client, refined_text, service_doc, max_variants=3):
    data_pairs = []

    # 1. 번호 있는 줄만 추출
    refined_commands = [
        re.sub(r"^\d+\.\s*", "", line).strip()
        for line in refined_text.split("\n")
        if re.match(r"^\d+\.\s*", line.strip())
    ]

    # 2. 명령어별 유사문장 및 코드 생성
    for idx, command in enumerate(refined_commands, start=1):
        #print(f"\n📌 명령어 {idx}: {command}")
        try:
            # 유사 문장 생성
            variants_text = expand_variants(client, command, n=max_variants)
            variants = [
                v.strip(" 1234567890.").strip()
                for v in variants_text.split("\n") if v.strip()
            ]
            all_variants = [command] + variants

            # 코드 생성
            current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
            code_obj = generate_python_from_text(client, command, service_doc, current_time)
            code_obj = transform_code(code_obj)[0]
            #print(code_obj)
            # 모든 문장에 동일한 코드 할당
            for variant in all_variants:
                data_pairs.append({
                    "text": variant,
                    "cron": code_obj.get("cron", ""),
                    "period": code_obj.get("period", -1),
                    "code": code_obj.get("code", code_obj if isinstance(code_obj, str) else "")
                })

        except Exception as e:
            print(f"❌ '{command}' 처리 실패: {e}")

    return data_pairs


# ===  GPT 프롬프트 구성 === #
# 1: 디바이스 스킬 기반 명령 생성
def generate_commands(client, skills_dict, n=10, examples=None):
    devices_str = json.dumps(skills_dict, indent=2, ensure_ascii=False)

    messages = load_prompt_roles(
        "generate_prompt.txt",
        devices=devices_str,
        n=n,
        examples=examples or ""
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()





# 2: 모호성 검사 및 수정
def refine_commands(client, commands_text):
    messages = load_prompt_roles("refine_prompt.txt", commands=commands_text)

    response = client.chat.completions.create(model="gpt-4", messages=messages, temperature=0.7)
    return response.choices[0].message.content.strip()



# 3: 유사 명령어 생성 
def expand_variants(client, command, n=3):
    messages = load_prompt_roles("variant_prompt.txt", command=command, n=n)

    response = client.chat.completions.create(model="gpt-4", messages=messages, temperature=0.8)
    return response.choices[0].message.content.strip()



# 4: 텍스트 명령어를 Python 코드로 변환 (prompt 템플릿 사용)
def generate_python_from_text(client, user_command, service_doc, current_time):
    prompt = f"""\
# Devices
{service_doc}

# User Command
command: {user_command}

# Current Time
current: {current_time}

# Output Format (SoPLang JSON)
Please generate a full SoPLang JSON block with:
- "cron"
- "period"
- "script"

"""
    messages = [
        {"role": "system", "content": grammar},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7
    )
    content = response.choices[0].message.content.strip()
    #print (content)
    return content

# def convert_dataset_to_joi_code(client, data_pairs):
#     joi_data = []

#     for i, pair in enumerate(data_pairs):
#         python_code = pair["code"]
#         text = pair["text"]

#         # GPT 프롬프트 구성
#         messages = load_prompt_roles("joi_prompt.txt", python_code=python_code)

#         try:
#             response = client.chat.completions.create(
#                 model="gpt-4",
#                 messages=messages,
#                 temperature=0.7
#             )
#             joi_code = response.choices[0].message.content.strip()

#             print(f"\n✅ 변환된 JOI Lang 코드 ({i+1}/{len(data_pairs)}):")
#             print(joi_code)

#         except Exception as e:
#             print(f"❌ JOI 변환 실패 (index {i}): {e}")
#             joi_code = None

#         joi_data.append({
#             "text": text,
#             "joi_code": joi_code
#         })
#     print(f"\n✅ 총 {len(joi_data)}개의 명령어-JOI 코드 쌍이 generated_dataset.json에 저장되었습니다.")
#     return joi_data

def convert_data_pairs_to_joi_pairs(data_pairs):
    joi_pairs = []
    for pair in data_pairs:
        print(pair)
        print(pair.get("cron"))
        text = pair["text"]
        cron = pair.get("cron", "")
        period = pair.get("period", -1)
        script_code = pair["script"]

        joi_item = transform_code(script_code)[0]
        joi_pairs.append({
            "text": text,
            "cron": cron,
            "period": period,
            "code": joi_item["code"]
        })

    return joi_pairs



def load_command_examples(folder_path, file_num, start=0, end=None):
    json_files = sorted(glob.glob(os.path.join(folder_path, f"category_{file_num}.json")))
    
    examples = []
    for file_path in json_files:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # 각 항목은 {"command": "..."} 형태라고 가정
            examples.extend([item["command"] for item in data if "command" in item])

    # 일부 샘플만 추출 (예: 5~10개)
    selected = examples[start:end] if end else examples
    #print(selected)
    return "\n".join([f"{i+1}. \"{text}\"" for i, text in enumerate(selected)])




# === 실행 === #
if __name__ == "__main__":
    device_docs = parse_class_docstrings("../0.1.3_docstring_v3.txt")
    sampled_device = sample_device_classes(device_docs, k=10)
    #print(sampled_device)
    
    folder = r"C:\Users\user\OneDrive\문서\GitHub\Project\Testset\Testset\json"
    examples = load_command_examples(folder, 3, start=6, end=10)
    
    base_commands = generate_commands(client, sampled_device, n=50, examples=examples)
    print("생성된 명령어들\n", base_commands)

    refined_text = refine_commands(client, base_commands)
    print("✅ 정제된 명령어들:\n", refined_text)
    
    data_pairs = process_refined_commands(client, refined_text, sampled_device, max_variants=3)
    #joi_code = convert_dataset_to_joi_code(client, data_pairs)
    #joi_code = convert_data_pairs_to_joi_pairs(data_pairs)
    
    # 🔽 파일로 저장
    with open("generated_dataset_3.json", "w", encoding="utf-8") as f:
        json.dump(data_pairs, f, ensure_ascii=False, indent=2)

    print(f"\n 총 {len(data_pairs)}개의 명령어-코드 쌍이 generated_dataset.json에 저장되었습니다.")
