# save it as 'main.py'
import ollama
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import requests
import json
from fastapi.staticfiles import StaticFiles

from pipeline_KO import run
# from pipeline import run
from time import time
def generate_code(sentence):
    return run.pipeline(sentence)
    


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SentenceInput(BaseModel):
    sentence: str





@app.post("/api/sentence_to_scenario")
def sentence_to_scenario(sentence_input: SentenceInput):
    print(f"input: {sentence_input.sentence}")
    scenario = generate_code(sentence_input.sentence)
    return {"scenario": scenario }



app.mount("/", StaticFiles(directory="static",html = True), name="static")
