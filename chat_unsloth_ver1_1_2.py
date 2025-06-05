import os, sys, re, gc, yaml, time, json
from datetime import datetime

from unsloth import FastLanguageModel
from unsloth.chat_templates import get_chat_template
from transformers import AutoTokenizer
from peft import PeftModel

from FlagEmbedding import BGEM3FlagModel
from Embedding.embedding import hybrid_recommend
from Grammar.grammar_ver1_1_5 import grammar
from Testset.joi_extraction_tool import parse_scenarios, extract_last_code_block
from Validation.validate import validate_tmp
from sentence_transformers import SentenceTransformer

from yaml.representer import SafeRepresenter

# --- YAML Literal 처리용 ---
class LiteralString(str): pass
def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
yaml.add_representer(LiteralString, literal_str_representer)


# --- 서비스 문서에서 디바이스 추출 ---
def extract_classes_by_name(text: str):
    pattern = r'Device\s+(\w+)\s*:\s*\n\s+"""(.*?)"""'
    matches = re.finditer(pattern, text, re.DOTALL)
    return {match.group(1): match.group(0) for match in matches}


# --- LLM 추론 ---
def run_test_case_unsloth(model, tokenizer, user_command_origin, user_command, classes, service_selected):
    current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
    messages = [{"role": "system", "content": grammar}] + \
               [{"role": "system", "content": classes[dev]} for dev in service_selected if dev in classes] + \
               [{"role": "user", "content": f"Current Time: {current_time}\nGenerate JOI Lang code for \"{user_command}\""}]

    tokenizer = get_chat_template(tokenizer, chat_template="chatml", map_eos_token=True)
    tokenizer.add_bos_token = False
    stop_tokens = ["<|im_end|>", "<|endoftext|>"]
    stop_token_ids = [tokenizer.convert_tokens_to_ids(token) for token in stop_tokens if token in tokenizer.get_vocab()]

    inputs = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt").to("cuda")

    start = time.time()
    outputs = model.generate(
        input_ids=inputs,
        eos_token_id=stop_token_ids,
        pad_token_id=tokenizer.pad_token_id,
        max_new_tokens=128,
        use_cache=True
    )
    elapsed = time.time() - start

    generated_ids = outputs[0][len(inputs[0]):]
    if generated_ids[-1].item() in stop_token_ids:
        generated_ids = generated_ids[:-1]
    response = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
    return response, elapsed


# --- 메인 루프 ---
def main():
    model_name = "qwenCoder"

    # 모델 로딩
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=f"./models/{model_name}-model",
        max_seq_length=4096,
        dtype=None,
        load_in_4bit=True,
    )
    model.load_adapter(f"./models/{model_name}-adapter")
    FastLanguageModel.for_inference(model)

    # 임베딩 및 유사도 모델 로딩
    model_bge = BGEM3FlagModel("./models/bge-m3", use_fp16=False, local_files_only=True)
    model_sentence = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    # 서비스 클래스 로딩
    with open("./ServiceExtraction/integration/service_list_ver1.1.8.txt", "r") as f:
        service_doc = f.read()
    classes = extract_classes_by_name(service_doc)

    # 테스트셋 루프
    for i in range(1, 2):  # 원하는 카테고리 범위 설정
        with open(f"./Testset/TestsetWithDevices_translated/category_{i}.yaml", "r") as f:
            results = []
            data = yaml.safe_load(f)

            for item in data:
                user_command = item["command_translated"]
                user_command_origin = item["command"]

                # 임베딩 기반 장치 선택
                start_bge = time.time()
                service_selected = set(r["key"] for r in hybrid_recommend(model_bge, user_command_origin, max_k=10))
                service_selected.add("Clock")
                bge_elapsed = time.time() - start_bge

                # LLM 호출
                resp, llm_elapsed = run_test_case_unsloth(
                    model, tokenizer, user_command_origin, user_command, classes, service_selected
                )

                # 코드 파싱
                try:
                    code = parse_scenarios(extract_last_code_block(resp))['code']
                except:
                    try:
                        code = parse_scenarios(resp)['code']
                    except:
                        code = [{'name': 'Scenario1', 'cron': '', 'period': -1, 'code': '(#AirConditioner).switch_on()\n'}]

                # 코드 정제 및 유효성 검사
                for c in code:
                    code_n = c["code"].strip()
                    code_n = validate_tmp(code_n, classes, list(service_selected), model_sentence)
                    c["code"] = LiteralString(code_n if code_n else "")

                entry = {
                    "command": user_command,
                    "devices": list(service_selected),
                    "generated_code": code,
                    "model_info": {
                        "elapsed_time": round(llm_elapsed + bge_elapsed, 3),
                        "bge_elapsed_time": round(bge_elapsed, 3),
                        "llm_elapsed_time": round(llm_elapsed, 3)
                    }
                }
                results.append(entry)

        # 저장
        os.makedirs(f"./Testset/Eval_{model_name}/", exist_ok=True)
        with open(f"./Testset/Eval_{model_name}/evaluation_category_{i}.yaml", "w", encoding="utf-8") as out_file:
            yaml.dump(results, out_file, indent=2, allow_unicode=True, sort_keys=False, width=float('inf'))

    del model
    gc.collect()

if __name__ == "__main__":
    main()
