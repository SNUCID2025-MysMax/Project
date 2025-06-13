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
import copy

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

    pattern = r'Device\s+(\w+)\s*:\s*"""(.*?)"""'
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
    output_path = f"trainset_yaml/generated_data_{file_num}.yaml"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(augmented_examples, f, indent=2, ensure_ascii=False)
    print(f"✅ {len(augmented_examples)}개의 예제가 {output_path}에 저장되었습니다.")
    return 
class LiteralString(str): pass

def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

yaml.add_representer(LiteralString, literal_str_representer)

def str_presenter(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)
yaml.add_representer(str, str_presenter)

# 2. YAML 전체 변환 함수
def convert_code_fields_to_literal_string(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith(".yaml"):
            file_path = os.path.join(folder_path, file)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)

                if not isinstance(data, list):
                    print(f"⚠️ Skipped {file}: not a list of items")
                    continue

                for item in data:
                    if "code" in item and isinstance(item["code"], list):
                        for block in item["code"]:
                            if isinstance(block.get("code"), str):
                                block["code"] = LiteralString(block["code"])

                with open(file_path, "w", encoding="utf-8") as f:
                    yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=float("inf"))

                print(f"✅ Converted: {file}")

            except Exception as e:
                print(f"❌ Failed to process {file}: {e}")


def update_command_for_period(command, new_period):
    seconds = new_period // 1000

    # 1. 특수 표현 정의
    custom_phrases = {
        30: ["every half a minute", "every half minute"],
        60: "every 1 minute",
    }

    # 2. 표현 선택
    if seconds in custom_phrases:
        phrase = custom_phrases[seconds]
        # 리스트일 경우 여러 표현 중 첫 번째로 선택
        if isinstance(phrase, list):
            phrase = phrase[0]
    elif seconds % 60 == 0:
        phrase = f"every {seconds // 60} minutes"
    else:
        phrase = f"every {seconds} seconds"

    # 3. 단어 기반 숫자 표현
    word_nums = r"(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|half)"
    time_units = r"(second[s]?|minute[s]?)"

    # 4. 주기 관련 정규식 패턴 (확장 가능)
    time_patterns = [
        fr"\b(every|at|once\s+every)\s+(?:\d+|{word_nums})\s*{time_units}",
        r"\bevery\s+\d+\s+seconds",
        r"\bevery\s+\d+\s+minutes",
        r"\bevery\s+half\s+(a\s+)?minute",
        r"\bevery\s+1\s+minute",
        r"\bevery\s+1\s+and\s+a\s+half\s+minutes",
        fr"\bat\s+(?:\d+|{word_nums})[- ]?second intervals",
        fr"\bintervals\s+of\s+(?:\d+|{word_nums})\s*{time_units}",
        fr"\bat\s+intervals\s+of\s+(?:\d+|{word_nums})\s*{time_units}"
    ]

    # 5. 하나의 정규식으로 병합
    time_pattern_regex = "(?i)" + "|".join(time_patterns)

    # 6. 대체 수행
    updated_command = re.sub(time_pattern_regex, phrase, command)
    return updated_command


def augment_period(item):
    original_period = item["code"][0]["period"]
    if original_period in [-1, 0, 100]:
        return None
    options = [v for v in range(1000, 60001, 1000) if v != original_period]
    if not options:
        return None
    new_period = random.choice(options)
    new_item = copy.deepcopy(item)
    new_item["code"][0]["period"] = new_period
    
    original_command = item.get("command", "")
    new_command = update_command_for_period(original_command, new_period)
    new_item["command"] = new_command
    
    return new_item

NUMBER_WORDS = {
    0: ["zero"],
    1: ["one"],
    2: ["two"],
    3: ["three"],
    4: ["four"],
    5: ["five"],
    6: ["six"],
    7: ["seven"],
    8: ["eight"],
    9: ["nine"],
    10: ["ten"],
    11: ["eleven"],
    12: ["twelve"],
    30: ["half"],  # 'half'는 30분 의미로 특별 처리 가능
}

WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


WEEKDAY_NAME_TO_NUM = {
    "monday": 1, "tuesday": 2, "wednesday": 3,
    "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7
}

WEEKDAY_NUM_TO_NAME = {
    1: "Monday", 2: "Tuesday", 3: "Wednesday",
    4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"
}

def shift_hour_range(hour_expr):
    """예: '8-23' → '9-23' 또는 '7-23' 중 랜덤"""
    start, end = map(int, hour_expr.split('-'))
    shift = random.choice([-1, 1])
    new_start = max(0, min(23, start + shift))
    new_range = f"{new_start}-{end}"
    return new_range, start, new_start

def shift_day_range(day_expr):
    """예: '1-5' → '2-6' 또는 '0-4'"""
    start, end = map(int, day_expr.split('-'))
    shift = random.choice([-1, 1])
    new_start = (start + shift - 1) % 7 + 1
    new_end = (end + shift - 1) % 7 + 1
    if new_end < new_start:
        new_start, new_end = new_end, new_start
    new_expr = f"{new_start}-{new_end}"
    return new_expr, f"{start}-{end}", f"{new_start}-{new_end}"
def to_ampm(hour: int):
    if hour < 12:
        return f"{hour}am"
    elif hour == 12:
        return "12pm"
    else:
        return f"{hour - 12}pm"
    
def update_command_for_cron_fields(command, hour_old=None, hour_new=None, day_old=None, day_new=None):
    new_command = command

    if hour_old is not None and hour_new is not None:
        old = str(hour_old)
        new = str(hour_new)
        ampm_old = to_ampm(hour_old)
        ampm_new = to_ampm(hour_new)
        # 1. 8am / 8 am → 7am
        pattern = re.compile(rf'\b{ampm_old}\b', re.IGNORECASE)
        new_command, count = pattern.subn(ampm_new, new_command)

        # 2. 단어형 (eight o'clock, eight in the morning 등)
        for num, words in NUMBER_WORDS.items():
            if num == int(old):
                for word in words:
                    pattern_word = re.compile(
                        rf'\b{word}(\s+(o\'clock|in the morning|in the evening))?\b',
                        re.IGNORECASE
                    )
                    new_command, count = pattern_word.subn(f"{new}", new_command, count=1)

        # 3. 그냥 숫자만 있는 경우: "from 8 to 23" 같은 곳
        pattern_plain = re.compile(rf'\b{old}\b')
        new_command, count = pattern_plain.subn(new, new_command, count=1)

    # ---- 요일 표현 치환 (기존 유지) ----
    if day_old is not None and day_new is not None:
        weekday_map_rev = {v: k for k, v in WEEKDAY_NAME_TO_NUM.items()}
        weekday_map = {k: v for v, k in WEEKDAY_NAME_TO_NUM.items()}  # 1: Monday ...

        def weekday_num_to_name(n):
            return weekday_map.get(int(n), None)

        # Case 1: 범위
        if isinstance(day_old, str) and '-' in day_old and isinstance(day_new, str) and '-' in day_new:
            old_start, old_end = map(int, day_old.split('-'))
            new_start, new_end = map(int, day_new.split('-'))

            old_exprs = [
                "weekdays" if (old_start, old_end) == (1, 5) else f"{weekday_num_to_name(old_start)} to {weekday_num_to_name(old_end)}",
                f"{weekday_num_to_name(old_start)} to {weekday_num_to_name(old_end)}"
            ]
            new_expr = (
                "weekdays" if (new_start, new_end) == (1, 5)
                else f"{weekday_num_to_name(new_start)} to {weekday_num_to_name(new_end)}"
            )
            for expr in old_exprs:
                if expr and expr.lower() in new_command.lower():
                    new_command = re.sub(re.escape(expr), new_expr, new_command, flags=re.IGNORECASE)

        # ✅ Case 2: 단일 숫자 요일
        else:
            try:
                old_day_num = int(day_old)
                new_day_num = int(day_new)
                old_day_name = weekday_num_to_name(old_day_num)
                new_day_name = weekday_num_to_name(new_day_num)
                if old_day_name and new_day_name:
                    pattern = re.compile(rf'\b(on|every|only)?\s*{old_day_name}\b', re.IGNORECASE)
                    new_command = pattern.sub(lambda m: f"{m.group(1) or ''} {new_day_name}".strip(), new_command)
            except Exception:
                pass
    return new_command





def augment_command_and_cron_multi(item):
    cron = item["code"][0]["cron"]
    command = item["command"]
    parts = cron.split()
    if len(parts) != 5:
        return []

    results = []
    original_parts = parts[:]  # 원본 유지

    hour_expr, day_expr = parts[1], parts[4]
    hour_augmented = False
    day_augmented = False

    # 1. 시간만 증강
    if '-' in hour_expr or hour_expr.isdigit() and hour_expr != "0":
        new_parts = original_parts[:]
        if '-' in hour_expr:
            hour_new_expr, hour_old_val, hour_new_val = shift_hour_range(hour_expr)
        else:
            hour_old_val = int(hour_expr)
            hour_new_val = max(0, min(23, hour_old_val + random.choice([-1, 1])))
            hour_new_expr = str(hour_new_val)
        new_parts[1] = hour_new_expr
        new_cron = ' '.join(new_parts)
        new_command = update_command_for_cron_fields(command, hour_old_val, hour_new_val, None, None)
        results.append(make_new_item(item, new_command, new_cron))
        hour_augmented = True

    # 2. 요일만 증강
    if ('-' in day_expr and day_expr != '*') or day_expr.isdigit():
        new_parts = original_parts[:]
        if '-' in day_expr and day_expr != '*':
            day_new_expr, day_old_val, day_new_val = shift_day_range(day_expr)
        else:
            day_old_val = int(day_expr)
            day_new_val = (day_old_val % 7) + 1
            day_new_expr = str(day_new_val)
        new_parts[4] = day_new_expr
        new_cron = ' '.join(new_parts)
        new_command = update_command_for_cron_fields(command, None, None, day_old_val, day_new_val)
        results.append(make_new_item(item, new_command, new_cron))
        day_augmented = True

    # 3. 시간 + 요일 둘 다 증강
    if hour_augmented and day_augmented:
        new_parts = original_parts[:]
        # 시간
        if '-' in hour_expr:
            hour_new_expr, hour_old_val, hour_new_val = shift_hour_range(hour_expr)
        else:
            hour_old_val = int(hour_expr)
            hour_new_val = max(0, min(23, hour_old_val + random.choice([-1, 1])))
            hour_new_expr = str(hour_new_val)
        new_parts[1] = hour_new_expr

        # 요일
        if '-' in day_expr and day_expr != '*':
            day_new_expr, day_old_val, day_new_val = shift_day_range(day_expr)
        else:
            day_old_val = int(day_expr)
            day_new_val = (day_old_val % 7) + 1
            day_new_expr = str(day_new_val)
        new_parts[4] = day_new_expr

        new_cron = ' '.join(new_parts)
        new_command = update_command_for_cron_fields(command, hour_old_val, hour_new_val, day_old_val, day_new_val)
        results.append(make_new_item(item, new_command, new_cron))

    return results


def make_new_item(item, new_command, new_cron):
    new_item = copy.deepcopy(item)
    new_item["command"] = new_command
    new_item["code"][0]["cron"] = new_cron
    return new_item


def augment_file(input_path, output_path):

    with open(input_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    original_count = len(data)
    all_results = []          # 원본 + 증강
    total_augmented = 0       # 증강된 항목만 카운트

    for item in data:
        pool = [copy.deepcopy(item)]   # 원본 포함

        # 1. period 증강
        p_aug = augment_period(item)
        if p_aug:
            pool.append(p_aug)
            total_augmented += 1
        

        # 2. cron 증강 (original + period 결과에 대해)
        new_cron_pool = []
        for it in pool:
            c_aug = augment_command_and_cron_multi(it)
            all_results.extend(c_aug)
            total_augmented += len(c_aug)
        all_results.append(copy.deepcopy(item))
        # # 3. code 증강 (모든 pool 대상)
        # for it in pool:
        #     n_augs = augment_code_numbers(it, k=3)
        #     final_new = [n for n in n_augs if n["code"][0]["code"] != it["code"][0]["code"]]
        #     total_augmented += len(final_new)
        #     all_results.extend(final_new)
            

    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(
            all_results,
            f,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
            width=1000
        )
        f.write(f"# original_count: {original_count}\n")
        f.write(f"# augmented_count: {total_augmented}\n")

           
def augment_all_files(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".yaml"):
            in_path = os.path.join(input_folder, filename)
            out_path = os.path.join(output_folder, filename)
            augment_file(in_path, out_path)
            print(f"✅ {filename} → augmented as {out_path}")
            
# === 실행 === #
if __name__ == "__main__":
    for i in range(1, 17):
        augment_file(
            f"trainset_yaml/generated_data_{i}.yaml",
            f"trainset_yaml_parameter/generated_data_{i}.yaml"
        )
    # device_docs = parse_class_docstrings("../../ServiceExtraction/integration/service_lis_ver1.1.8.txt")
    # file_num = 6
    # for i in range(5,6):
    #     file_num = i
    #     examples = load_command_examples(file_num, start=5, end=10)
    #     generated_examples = generate_variants(examples, device_docs)
    #     augmented_examples = augment_commands_only(generated_examples, client, n=3)
    #     save_augmented_examples_to_trainset(augmented_examples, file_num)

    