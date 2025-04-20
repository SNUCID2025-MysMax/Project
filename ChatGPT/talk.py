from openai import OpenAI
import tqdm
import os

# OpenAI API 키 설정 (환경 변수 또는 직접 삽입)
client = OpenAI(api_key="apikey")  # 또는 'sk-...'

prompt = "hello?"

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful SoPLang code generator."},
        {"role": "user", "content": prompt}
    ]
)

resp = response.choices[0].message.content
print(resp)