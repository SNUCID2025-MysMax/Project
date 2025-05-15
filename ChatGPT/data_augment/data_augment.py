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
# 환경 변수 로드
load_dotenv()
api_key = os.getenv("apikey")


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
#def extract_device_skills(filepath):
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
        print(f"\n📌 명령어 {idx}: {command}")
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
            code = generate_python_from_text(client, command, service_doc, current_time)

            # 모든 문장에 동일한 코드 할당
            for i, variant in enumerate(all_variants):
                print(f"  {i+1}. {variant}")
                data_pairs.append({"text": variant, "code": code})

        except Exception as e:
            print(f"❌ '{command}' 처리 실패: {e}")

    return data_pairs


# ===  GPT 프롬프트 구성 === #
# 1: 디바이스 스킬 기반 명령 생성
def generate_commands(client, skills_dict, n=10):
    devices_str = json.dumps(skills_dict, indent=2, ensure_ascii=False)
    messages = load_prompt_roles("generate_prompt.txt", devices=devices_str, n=n)

    response = client.chat.completions.create(model="gpt-4", messages=messages, temperature=0.7)
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
    return response.choices[0].message.content.strip()



# === 실행 === #
if __name__ == "__main__":
    device_docs = parse_class_docstrings("../0.1.3_docstring_v3.txt")
    sampled_device = sample_device_classes(device_docs, k=3)

    base_commands = generate_commands(client, sampled_device, n=5)
    print("생성된 명령어들\n", base_commands)

    refined_text = refine_commands(client, base_commands)
    print("✅ 정제된 명령어들:\n", refined_text)
    
    data_pairs = process_refined_commands(client, refined_text, sampled_device, max_variants=3)

    # 🔽 파일로 저장
    with open("generated_dataset.json", "w", encoding="utf-8") as f:
        json.dump(data_pairs, f, ensure_ascii=False, indent=2)

    print(f"\n 총 {len(data_pairs)}개의 명령어-코드 쌍이 generated_dataset.json에 저장되었습니다.")
