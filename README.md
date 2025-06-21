# 25-1 창통설 I조 - JOI Lang 코드 생성 모델 개발

- 완성된 프로젝트 서버 레포: [JOI_Lang_Generator](https://github.com/SNUCID2025-MysMax/JOI_Lang_Generator)
- 최종 어댑터 레포: [endermaru/mysmax](https://huggingface.co/endermaru/mysmax)

## 개발 환경
- AWS ec2 g6.xlarge: 24GB VRAM의 L4 GPU 1개 탑재
- 파이썬 가상환경(venv) 사용

## 디렉토리 및 파일 설명

- Notion의 프로젝트 페이지 참고 필요
- 최종 버전은 서버 레포에 작성되어 있음

### 파일
- `chat_gpt.py`(deprecated): openai API 기반 테스트
- `chat_ollama_ver*.py`(deprecated): ollama 기반 테스트
- `chat_unsloth_ver*.py`: 모델 & 어댑터 로드 후 테스트
    - 1_1_2는 직접 테스트케이스를 불러와 테스트
    - 1_1_3은 [JOI_Lang_Generator](https://github.com/SNUCID2025-MysMax/JOI_Lang_Generator) 서버를 띄운 뒤 localhost로 호출(로컬과 클라우드 테스트 가능) + Evaluation 모듈을 이용한 평가 가능

### 디렉토리
#### `ChatGPT`: OpenAI API를 이용한 테스트셋 및 증강 데이터셋
- 증강한 데이터셋은 `data_augment`에 존재
    - `trainset_json`과 `trainset_yaml`은 GPT 기반 증강
    - `trainset_yaml_parameter`는 GPT 기반 증강 + 파라미터 대체를 통한 증강 (최종 데이터셋)

#### `Conversion`(deprecated): 모델이 파이썬 코드를 생성하면 이를 추출, JOI Lang으로 변환하는 코드
- Grammar_ver1_1_3에 기반하여 진행하였으나 정확도 하락으로 폐기

#### `Demo`: 회사에서 수행한 Demo를 위한 디렉토리
- 직접 개발한 Script Similarity(Evaluation 모듈)과 회사에서 제공한 Cloud Similarity 기반 평가를 진행하였음
- `final_output_250616_filtered_result_all.csv`에 최종 결과가 저장됨

#### `Embedding`: 명령어 기반 디바이스 추출을 위한 임베딩을 진행한 디렉토리
- 디바이스 임베딩은 루트의 `ServiceExtraction/integration/service_list_ver1.1.6*` 기반으로 수행됨
- `embedding_notebook.ipynb`에서 모든 임베딩 버전을 시도하였음
- `embedding_result_v4`, `embedding_v4`가 최종 버전으로 JOI_Lang_Generator에 포함

#### `Evaluation`: 다양한 평가 기준을 통해 코드 평가를 수행하는 디렉토리
- `compare_soplang_ir.py`에 핵심 함수가 정의되어 있음
- 사용방법은 루트의 `chat_unsloth_ver1_1_3.py`의 `main` 참고

#### `finetune`: Unsloth 라이브러리의 LoRA 파인튜닝 진행
- `finetune_qwencoder_instruct.py`가 최종 버전
- 파인튜닝이 완료된 모델 어댑터는 루트의 `model`에 저장됨
- 양자화된 `gguf` 변환을 시도하였으나 매우 큰 용량, 메모리, 시간 등으로 채택하지 않음

#### `Grammar`: JOI Lang 문법 프롬프트의 다양한 버전을 다룬 디렉토리
- 현재 서버 레포에서는 1_1_8 버전 사용
- 이를 더 개선한 1_1_9(Chain of Draft), 1_1_10(마크다운 개선) 등이 있지만 실제로 사용되지 않음

#### `(models)`(.gitignore): 파인튜닝, 다운로드 받은 모델을 저장하는 디렉토리 - 경우에 따라 추가 필요

#### `OldVersion`: 24년도 창통설의 이전 프로젝트의 파이프라인을 가져와 테스트 진행
- 기존 방식에서 codellama, exaone, 한국어 데이터셋 등을 새로 도입해 테스트 진행

#### `ServiceExtraction`: JOI 플랫폼에서 지원하는 디바이스와 스킬(서비스) 정보를 바탕으로 디바이스 DocString을 생성
- `integration` 폴더 내부에 디바이스 정보를 json, 문자열 형식의 여러 버전의 DocString이 존재
- 현재 서버 레포에서는 1.1.9 버전 사용
- `integration/extraction.ipynb` 기반으로 Python 클래스 형식의 디바이스, 스킬을 추출, 파싱을 진행하였음

#### `Testset`: 카테고리 0~16에 대해 카테고리0 238개, 나머지 카테고리 10개로 총 398개의 테스트셋을 다루는 디렉토리
- `TestsetWithDevices_translated`에 완성된 테스트셋이 있습니다. 각 케이스별 한국어 문장, 영어문장, 코드(name,period,code,cron), 필요한 디바이스 목록이 yaml 형식으로 저장됨
- 파인튜닝에는 카테고리0 전체와 나머지 카테고리의 각 5개(6~10번)가 사용됨
- `Eval_*`에는 각 모델 별 테스트셋 기반 코드 생성한 결과가 저장되어 있음. 몇 개의 경우 evaluation 모듈에 기반한 분석결과가 포함되어 있음.
- 그 외의 기타 파일들은 테스트셋을 다루는 데 사용된 여러 시도가 담긴 코드(번역, 파싱 등)

#### `Validation`: 생성된 코드 텍스트에 대한 검증을 수행. 완성된 모듈은 JOI_Lang_Generator 레포에 포함되어 있음

---
## Extra branch
- 몇 가지 개선점을 적용했으나 성능적으로 유의미한 차이가 없음
1. grammar_1_1_10으로 cron, period를 재정의, # 제거, Chain of Draft 도입
2. 분리 케이스 제외: 평가 모듈도 분리에 잘 대응하지 못 함
3. 테스트셋 필터링: 분리(12), 너무 복잡한 케이스(15), 의미 없는 카테고리(14,16)

- Eval_qwenCoder_250621은 낮은 lr, lora_alpha
- Eval_qwenCoder_250621-2는 높은 lr, lora_alpah(과적합 가능성 있음)