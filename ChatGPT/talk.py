from openai import OpenAI
from dotenv import load_dotenv
import os, sys, re
from grammar import grammar
import tiktoken
from embedding import hybrid_recommend

# .env 파일에서 환경변수 불러오기
load_dotenv()

def extract_classes_by_name(text: str):
    pattern = r'class\s+(\w+)\s*:\s*\n\s+"""(.*?)"""'
    matches = re.finditer(pattern, text, re.DOTALL)

    class_dict = {}
    for match in matches:
        class_name = match.group(1)
        full_class_def = match.group(0)  # 전체 클래스 문자열
        class_dict[class_name] = full_class_def

    return class_dict

with open("../ServiceExtraction/integration/0.1.3_docstring_v3.txt", "r") as f:
    service_doc = f.read()

classes = extract_classes_by_name(service_doc)

current_time = "10:00:00 04.25. 6"
if False:
    user_command = input()
else:
    user_command = "내일 오전 10시에 알람 설정해줘"

service_selected = set(i["key"] for i in hybrid_recommend(user_command, max_k=7))
service_selected.add("Clock")
service_doc = "\n".join([classes[i] for i in service_selected])


prompt = f"{grammar}\n---\n# Service List\n{service_doc}"

# encoding = tiktoken.encoding_for_model("gpt-4")
# text = f"{grammar}\n---\n{service_doc}\ncommand: {user_command}\ncurrent: {current_time}"
# num_tokens = len(encoding.encode(text))
# print(f"총 토큰 수: {num_tokens}")

# 환경 변수에서 API 키 읽기
api_key = os.getenv("apikey")

# 클라이언트 생성
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"command: {user_command}\ncurrent: {current_time}"},
    ]
)

resp = response.choices[0].message.content
print("응답:", resp)

print("모델:", response.model)
print("생성 시각:", response.created)
print("Finish Reason:", response.choices[0].finish_reason)
print("토큰 사용량:")
print(" - prompt:", response.usage.prompt_tokens)
print(" - completion:", response.usage.completion_tokens)
print(" - total:", response.usage.total_tokens)