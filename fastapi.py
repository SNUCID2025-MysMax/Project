from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict, Optional
from datetime import datetime

app = FastAPI()

# 요청 스키마 정의
class GenerateCodeRequest(BaseModel):
    sentence: str
    model: str
    connected_devices: Dict
    current_time: Optional[str] = None
    options: Optional[str] = ""

# 응답 스키마는 생략 가능 (자동으로 추론됨)

@app.post("/generate-code")
def generate_code(req: GenerateCodeRequest):
    # 현재 시간이 안 들어오면 자동 생성
    now = req.current_time or datetime.now().isoformat()

    result = generate_joi_code(
        sentence=req.sentence,
        model=req.model,
        connected_devices=req.connected_devices,
        current_time=now,
        other_params=None
    )
    return result

# 기존 로직
def generate_joi_code(sentence: str, model: str, connected_devices: dict, current_time: str, other_params: dict = None) -> dict:
    return {
        "code": [
            {
                "name": "Scenario1",
                "cron": "0 9 * * *",
                "period": -1,
                "code": "(#Light #livingroom).switch_on()"
            },
            {
                "name": "Scenario2",
                "cron": "0 9 * * *",
                "period": 10000,
                "code": "(#Light #livingroom).switch_on()"
            }
        ],
        "log": {
            "response_time": "0.321 seconds",
            "inference_time": "0.279 seconds",
            "translated_sentence": sentence,
            "mapped_devices": [
                "virtual_light_livingroom_1",
                "virtual_light_livingroom_2"
            ]
        }
    }
