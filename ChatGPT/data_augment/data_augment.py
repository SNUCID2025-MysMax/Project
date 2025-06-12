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
from yaml.representer import SafeRepresenter

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
    # print(response.choices[0].message.content.strip())
    # print("Input tokens:", usage.prompt_tokens)
    # print("Output tokens:", usage.completion_tokens)
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
    # print("  Prompt tokens   :", response.usage.prompt_tokens)
    # print("  Completion tokens:", response.usage.completion_tokens)
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



def load_command_examples(file_num, start=0, end=None):
    folder_path = r"C:\Users\김지후\Downloads\testt\Project\Testset\TestsetWithDevices_translated"
    yaml_file = os.path.join(folder_path, f"category_{file_num}.yaml")
    
    examples = []
    if os.path.exists(yaml_file):
        with open(yaml_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            examples.extend(data)

    selected = examples[start:end] if end else examples
    return selected


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

def extract_device_definitions(devices, device_docs):
    selected_definitions = []

    for dev in devices:
        if dev in device_docs:
            selected_definitions.append(device_docs[dev])
        else:
            print(f"[WARN] '{dev}' not found in device_docs")

    return "\n\n".join(selected_definitions)

def generate_variants(examples, device_docs):
    prompt_path = "device_variants.txt"  
    updated_examples = []

    for example in examples:
        devices = example["devices"]
        code_entry = example["code"][0]
        original_command = example["command_translated"]
        original_code = code_entry["code"]

        selected_devices = extract_device_definitions(devices, device_docs)

        messages = load_prompt_roles(
            path=prompt_path,
            device_classes=selected_devices,
            original_command = original_command,
            original_code=original_code
        )

        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7
        )
        content = response.choices[0].message.content.strip()
        # print("  Prompt tokens   :", response.usage.prompt_tokens)
        # print("  Completion tokens:", response.usage.completion_tokens)
        
        variants = re.split(r"\n---+\s*", content)
        
        for variant in variants:
            if not variant.strip():
                continue  # 빈 블록 무시

            english_match = re.search(r"(?i)ENGLISH:\s*(.*?)\s*CODE:", variant, re.DOTALL)
            code_match = re.search(r"(?i)CODE:\s*(.*)", variant, re.DOTALL)

            if not english_match or not code_match:
                print("[WARN] Skipped malformed variant:\n", variant)
                continue

            new_command = english_match.group(1).strip()
            new_code = code_match.group(1).strip()

            updated_example = {
                "command": new_command,
                "code": [{
                    **code_entry,
                    "code": new_code
                }]
            }

            updated_examples.append(updated_example)

    return updated_examples
def augment_commands_only(generated_examples, client, n=3):
    augmented = []

    for example in generated_examples:
        base_command = example["command"]
        code_copy = example["code"]

        # GPT로 command paraphrase 확장
        try:
            variants_text = expand_variants(client, base_command, n=n)
            variants = [
                v.strip(" 1234567890.-").strip()
                for v in variants_text.split("\n")
                if v.strip()
            ]
            all_commands = [base_command] + variants  # 원본도 포함

            for cmd in all_commands:
                augmented.append({
                    "command": cmd,
                    "code": code_copy
                })

        except Exception as e:
            print(f"[❌] Command augmentation failed: {base_command}\n{e}")

    return augmented

def apply_parameter_tuning_and_save(augmented_examples, client, num, prompt_path="parameter_tuning.txt"):
    os.makedirs("trainset", exist_ok=True)
    total_variants = []
    for example in augmented_examples:
        script_code = example["code"][0]["code"]
        messages = load_prompt_roles(
            path=prompt_path,
            original_code=script_code,
        )

        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7
        )
        print("  Prompt tokens   :", response.usage.prompt_tokens)
        print("  Completion tokens:", response.usage.completion_tokens)

        content = response.choices[0].message.content.strip()
        print(content)
        # --- 구분자 기준으로 여러 variant 추출
        variants = []
        for block in re.split(r"\n---+\s*", content):
            if not block.strip():
                continue

            match_eng = re.search(r"(?i)ENGLISH:\s*(.*?)\s*CODE:", block, re.DOTALL)
            match_code = re.search(r"(?i)CODE:\s*(.*)", block, re.DOTALL)
            if not match_eng or not match_code:
                print(f"[WARN] Skipping unparsable block:\n{block}")
                continue
            script_body = match_code.group(1).strip()

            # cron과 period 값 파싱 시도
            cron_match = re.search(r'"?cron"?\s*:\s*"([^"]*)"', script_body)
            period_match = re.search(r'"?period"?\s*:\s*(-?\d+)', script_body)

            cron = cron_match.group(1).strip() if cron_match else example["code"][0]["cron"]
            period = int(period_match.group(1)) if period_match else example["code"][0]["period"]

            variants.append({
                "command": match_eng.group(1).strip(),
                "code": [{
                    "name": example["code"][0]["name"],
                    "cron": cron,
                    "period": period,
                    "code": script_body
                }]
            })
            
        output_examples = variants if variants else [example]
        total_variants.extend(output_examples)
        
        output_path = f"trainset/generated_data_{num}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(variants, f, indent=2, ensure_ascii=False)

    return print(f"\n 총 {len(total_variants)}개의 명령어-코드 쌍이 generated_dataset_1.json에 저장되었습니다.")
def tune_examples_pythonically(augmented_examples):
    cron_options = ["0 10 * * *", "0 18 * * *"]
    period_options = [15000, 20000]
    param_range = range(10, 41, 5)  # 예: 10~40 사이 숫자

    tuned = []

    for ex in augmented_examples:
        base = ex.copy()
        code_block = base["code"][0]

        # 1. cron 튜닝 (존재하면)
        if code_block["cron"].strip():
            code_block["cron"] = random.choice(cron_options)

        # 2. period 튜닝 (단, -1 또는 100이면 유지)
        if code_block["period"] not in [-1, 100]:
            code_block["period"] = random.choice(period_options)

        # 3. parameter (숫자) 치환
        code_str = code_block["code"]

        # 정규식으로 '== 숫자' 패턴 찾아서 랜덤 값으로 치환
        def replace_param(match):
            old_val = match.group(1)
            new_val = str(random.choice(param_range))
            return f"== {new_val}"

        new_code = re.sub(r"==\s*(\d+)", replace_param, code_str)
        code_block["code"] = new_code

        tuned.append(base)

    return tuned

def save_augmented_examples_to_trainset(augmented_examples, file_num=1):
    os.makedirs("trainset", exist_ok=True)
    output_path = f"trainset/generated_data_{file_num}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(augmented_examples, f, indent=2, ensure_ascii=False)
    print(f"✅ {len(augmented_examples)}개의 예제가 {output_path}에 저장되었습니다.")
    return 

# === 실행 === #
if __name__ == "__main__":
    device_docs = parse_class_docstrings("../0.1.3_docstring_v3.txt")
    file_num = 6
    for i in range(3,4):
        file_num = i
        examples = load_command_examples(file_num, start=5, end=10)
        generated_examples = generate_variants(examples, device_docs)
        augmented_examples = augment_commands_only(generated_examples, client, n=3)
        save_augmented_examples_to_trainset(augmented_examples, file_num)
    #apply_parameter_tuning_and_save(augmented_examples, client, file_num)

    