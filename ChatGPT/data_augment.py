from openai import OpenAI
from dotenv import load_dotenv
import ast
import os
from datetime import datetime
import json

# 환경 변수 로드
load_dotenv()
api_key = os.getenv("apikey")

#print("API KEY:", api_key)
client = OpenAI(api_key=api_key)
'''
# 📌 증강할 시나리오 (자연어 명령)
base_scenarios = [
    "밤 10시가 되면 불을 꺼줘",
    "아침 6시에 스프링클러를 작동시켜줘",
    "온실 온도가 30도 이상이면 환풍기를 켜줘",
]

# 📌 프롬프트 템플릿: 문장 스타일 다양화 유도
def build_prompt(sentence):
    return f"""너는 스마트팜을 제어하는 사용자 명령어를 다양한 문장 스타일로 바꿔주는 역할이야.
다음 문장을 기반으로, **같은 의미**를 갖되 **다른 표현 방식**으로 5개 문장을 만들어줘.

예시:  
입력: 밤 10시가 되면 불을 꺼줘  
출력:  
1. 밤 열 시에 자동으로 조명을 꺼줘  
2. 불을 밤 10시에 꺼줘  
3. 22시에 조명 꺼짐 동작을 실행해줘  
4. 밤 10시 정각에 조명을 종료해줘  
5. 밤 10시에 자동 소등해줘

입력:
{sentence}

출력:"""

# 결과 저장 리스트
augmented_results = []

# 증강 실행
for sentence in base_scenarios:
    prompt = build_prompt(sentence)

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "너는 스마트팜 음성 명령어 리라이팅 도우미야."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.9
        )
        output = response.choices[0].message.content.strip()
        print(f"\n📝 원본: {sentence}\n📎 GPT 출력:\n{output}")
        augmented_results.append({
            "original": sentence,
            "augmented": output
        })

    except Exception as e:
        print(f"❌ GPT 호출 실패: {e}")
'''

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



# ===  GPT 프롬프트 구성 === #
def build_prompt_from_skills(skills_dict, n=10):
    prompt = (
        f"이 장치들과 기능들을 조합해서, 사람이 음성으로 요청할 것 같은 자연어 명령어를 {n}개 만들어줘.\n"
        "조건, 시간, 센서, 모드 등 다양한 상황을 반영해서 작성해줘.\n"
        "단, 다음과 같은 모호성은 피해야 해:\n"
        "- 수치 모호성: '높다', '낮다' 대신 구체적인 값 사용 (예: 온도가 30도 이상)\n"
        "- 시점 모호성: '저녁', '아침' 대신 구체적인 시간 사용 (예: 오전 7시)\n"
        "- 문장 구조 모호성: 순서나 조건이 헷갈리지 않도록 명확한 표현 사용\n"
        "- 복합 명령 모호성: 명령이 2개 이상일 경우, 명확히 나누거나 구체적으로 설명\n"
        "문법적으로 자연스러운 문장만 생성해줘.\n\n"
    )

    prompt += "사용 가능한 장치 및 기능 목록:\n"
    for device, methods in skills_dict.items():
        method_list = ', '.join(methods)
        prompt += f"- {device}: {method_list}\n"

    prompt += "\n출력 예시:\n"
    prompt += "1. 아침 7시에 조명을 켜줘\n"
    prompt += "2. 온도가 30도 이상이면 에어컨을 켜줘\n"
    prompt += "...\n"

    return prompt

def gpt_call(prompt, system="", temperature = 0.7):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

# 1: 디바이스 스킬 기반 명령 생성
def generate_commands(skills_dict, n=10):
    prompt = (
        f"아래는 사용할 수 있는 장치들과 기능입니다.\n"
        f"{json.dumps(skills_dict, indent=2, ensure_ascii=False)}\n\n"
        f"이 장치들과 기능을 활용한 자연어 명령어를 {n}개 생성해줘. "
        f"명확한 수치와 시간 표현을 사용하고, 문장이 모호하지 않게 작성해줘.\n"
        f"예: '오전 7시에 조명을 켜줘', '온도가 30도 이상이면 에어컨을 켜줘'\n"
    )
    return gpt_call(prompt, system="너는 스마트팜 명령어 생성기야.")


# 2: 모호성 검사 및 수정
def refine_commands(commands_text):
    prompt = (
        f"각 문장을 읽고, 모호하거나 불명확한 표현이 있다면 자연스럽고 명확한 문장으로 고쳐줘.\n"
        f"모호하지 않은 문장은 그대로 유지하고, 모두 같은 형식으로 출력해줘.\n"
        f"결과는 숫자 목록 형태로 간결하게 보여줘 (예: 1. 명령어... 2. 명령어...).\n\n"
        f"{commands_text}"
    )
    return gpt_call(prompt, system="너는 명령어 모호성 검열기야.")


# 3: 유사 명령어 생성 
def expand_variants(command, n = 3):
    prompt = (
        f"다음 명령어와 의미는 같지만 다른 표현 {n}개를 만들어줘:\n'{command}'"
    )
    return gpt_call(prompt, system="너는 명령어 스타일 확장기야.")


#  4: JSON 명령어로 변환
def to_joilang(natural_command):
    prompt = (
        f"다음 자연어 명령을 스마트팜 제어용 joi lang으로 변환해줘. "
    )
    return gpt_call(prompt, system="너는 명령어 → Joi lang 변환기야.")

# ===  실행 === #
if __name__ == "__main__":
    skills = extract_device_skills("device_model.py")
    #for device, skill_list in skills.items():
    #    print(f"- {device}: {', '.join(skill_list)}")
    
    base_commands = generate_commands(skills, n=10)
    print("생성된 명령어들\n", base_commands)

    refined = refine_commands(base_commands)

    for idx, command in enumerate(refined.split("\n"), start=1):
        print(f"\n 명령어 {idx}: {command}")

        # 유사 명령어 생성
        variants_text = expand_variants(command)
        variants = [v.strip(" 12345.").strip() for v in variants_text.split("\n") if v.strip()]

        for i, variant in enumerate(variants, 1):
            print(f"  {i}. {variant}")