from openai import OpenAI
from dotenv import load_dotenv
import ast
import os
from datetime import datetime
import json
import re
import sys
import random
from conversion import transform_code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from grammar import grammar
from conversion import transform_code
import yaml

load_dotenv()
apikey = os.getenv("OPENAI_API_KEY")

#print("🔍 Loaded API Key:", apikey)
client = OpenAI(api_key=apikey)

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

def process_refined_commands(client, base_commands, service_doc, max_variants):
    data_pairs = []
    if isinstance(base_commands, str):
        base_commands = [
            line.strip(" 1234567890.-").strip()
            for line in base_commands.split("\n")
            if line.strip()
        ]
    for command in base_commands:
        #print(command)
        try:
            # 유사 문장 생성
            variants_text = expand_variants(client, command, n=max_variants)
            variants = [
                v.strip(" 1234567890.").strip()
                for v in variants_text.split("\n") if v.strip()
            ]
            all_variants = [command] + variants
            #print(all_variants)

            # 코드 생성
            current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
            code_obj = generate_python_from_text(client, command, service_doc, current_time)
            code_obj = transform_code(code_obj)[0]

            for variant in all_variants:
                data_pairs.append({"text": variant, "code": code_obj})


        except Exception as e:
            print(f"❌ '{command}' 처리 실패: {e}")

    return data_pairs


# ===  GPT 프롬프트 구성 === #
# 1: 디바이스 스킬 기반 명령 생성


def generate_commands(client, skills_dict, n, examples="", category_context=""):
    devices_str = json.dumps(skills_dict, indent=2, ensure_ascii=False)
    if isinstance(examples, list):
        examples = "\n".join(f"{i+1}. {ex}" for i, ex in enumerate(examples))
    messages = load_prompt_roles(
        "generate_prompt_english.txt", 
        devices=devices_str, 
        n=n, 
        examples=examples, 
        context=category_context
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
    )
    usage = response.usage
    print(response.choices[0].message.content.strip())
    print("Input tokens:", usage.prompt_tokens)
    print("Output tokens:", usage.completion_tokens)
    return response.choices[0].message.content.strip()





# 2: 모호성 검사 및 수정
def refine_commands(client, commands_text):
    messages = load_prompt_roles("refine_prompt.txt", commands=commands_text)

    response = client.chat.completions.create(model="gpt-4", messages=messages, temperature=0.7)
    return response.choices[0].message.content.strip()



# 3: 유사 명령어 생성 
def expand_variants(client, example, n):
    messages = load_prompt_roles("variant_prompt_english.txt", command=example, n=n)
    
    response = client.chat.completions.create(model="gpt-4", messages=messages, temperature=0.8)
    usage = response.usage
    print(response.choices[0].message.content.strip())
    print("Input tokens:", usage.prompt_tokens)
    print("Output tokens:", usage.completion_tokens)
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
    usage = response.usage
    print(response.choices[0].message.content.strip())
    print("Input tokens:", usage.prompt_tokens)
    print("Output tokens:", usage.completion_tokens)
    content = response.choices[0].message.content.strip()
    
    return content

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



def load_command_examples(folder_path, file_num, start=0, end=None, context_map=None):
    yaml_file = os.path.join(folder_path, f"category_{file_num}.yaml")
    
    examples = []
    if os.path.exists(yaml_file):
        with open(yaml_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            examples.extend([item["command_translated"] for item in data if "command_translated" in item])

    selected = examples[start:end] if end else examples
    category_context = context_map[file_num] if context_map and file_num in context_map else ""
    return selected, category_context


# 5: Python code 를 joi_lang 으로 변환
def convert_to_joi_lang(data_pairs):
    joi_pairs = []

    for pair in data_pairs:
        python_code = pair["code"]
        try:
            joi_result = transform_code(python_code)
            if joi_result:
                joi_code = joi_result[0]["code"]
                joi_pairs.append({
                    "text": pair["text"],
                    "code": joi_code
                })
            else:
                print(f"⚠️ 변환 실패 (결과 없음): {pair['text']}")
        except Exception as e:
            print(f"❌ 변환 중 오류 발생: {e} — {pair['text']}")

    return joi_pairs

# 6: 예시 변수 로드
def load_example_variables(path):
    with open(path, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source)

    result = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            var_name = node.targets[0].id
            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                result[var_name] = node.value.value.strip()
    return result

def load_category_contexts(json_file_path):
    with open(json_file_path, "r", encoding="utf-8") as f:
        return {int(k): v for k, v in json.load(f).items()}

# === 실행 === #
if __name__ == "__main__":
    device_docs = parse_class_docstrings("../0.1.3_docstring_v3.txt")
    sampled_device = sample_device_classes(device_docs, k=10)

    folder = r"C:\Users\김지후\Downloads\testt\Project\Testset\TestsetWithDevices_translated"
    context_map = load_category_contexts("category_contexts.json")
    examples, category_context = load_command_examples(folder, 1, start=5, end=10)
    #print(examples)
    base_commands = generate_commands(client, sampled_device, n=1, examples=examples, category_context = category_context)
    with open("generated_dataset_1.json", "w", encoding="utf-8") as f:
         json.dump(base_commands, f, ensure_ascii=False, indent=2)
    # data_pairs = process_refined_commands(client, base_commands, sampled_device, max_variants=1)
    
    # # # 🔽 파일로 저장
    # with open("generated_dataset_1.json", "w", encoding="utf-8") as f:
    #     json.dump(data_pairs, f, ensure_ascii=False, indent=2)

    print(f"\n 총 {len(data_pairs)}개의 명령어-코드 쌍이 generated_dataset_1.json에 저장되었습니다.")

