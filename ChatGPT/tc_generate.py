from openai import OpenAI
from dotenv import load_dotenv
import os, sys, re, gc
from datetime import datetime
from grammar import grammar, grammar_compressed
import tiktoken
from embedding import hybrid_recommend
from conversion import transform_code
from FlagEmbedding import BGEM3FlagModel
import json

CATEGORY_NUM = 15

# .env 파일에서 환경변수 불러오기
load_dotenv()


# Load Embedding
model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=False)
    

with open("TestCase\\main_prompt.txt", "r", encoding="utf-8") as f:
    main_prompt = f.read()
    
with open("TestCase\\category_prompt.txt", "r", encoding="utf-8") as f:
    category_prompt = f.read()

with open("TestCase\\generate_prompt.txt", "r", encoding="utf-8") as f:
    generate_prompt = f.read()


pattern = r"\[Category\s+\d+:.*?(?=\n\[Category\s+\d+:|\Z)"  # 다음 카테고리 시작 또는 파일 끝까지
categories = re.findall(pattern, category_prompt, re.DOTALL)



for i, cat in enumerate(categories):
    
    # 환경 변수에서 API 키 읽기
    api_key = os.getenv("apikey")

    # 클라이언트 생성
    client = OpenAI(api_key=api_key)
    
    client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": main_prompt}
        ]
    )
    client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": cat}
        ]
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": generate_prompt%i}
        ]
    )

    resp = response.choices[0].message.content
    print(resp)
            
        





    
    
del model
gc.collect()