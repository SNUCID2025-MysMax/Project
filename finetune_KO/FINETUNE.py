import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer
from datasets import Dataset

# 모델 로딩 설정
model_name = "LGAI-EXAONE/EXAONE-Deep-7.8B"
max_seq_length = 2048
load_in_4bit = True  # 메모리 사용량 줄이기 위한 4비트 양자화

# 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

# 모델 로드
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
    load_in_4bit=load_in_4bit
)

# 그래디언트 체크포인팅 활성화 및 4비트 학습 준비
model.gradient_checkpointing_enable()
if load_in_4bit:
    model = prepare_model_for_kbit_training(model)

# LoRA 설정
lora_config = LoraConfig(
    r=16,  # LoRA 랭크
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# LoRA 모델 생성
model = get_peft_model(model, lora_config)
print(model.print_trainable_parameters())

# 데이터 포맷팅 함수
def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = []
    
    for convo in convos:
        formatted_convo = []
        for turn in convo:
            if turn["from"] == "human":
                formatted_convo.append({"role": "user", "content": turn["value"]})
            elif turn["from"] == "gpt":
                formatted_convo.append({"role": "assistant", "content": turn["value"]})
        
        # EXAONE 모델의 채팅 템플릿 적용
        text = tokenizer.apply_chat_template(
            formatted_convo,
            tokenize=False,
            add_generation_prompt=False
        )
        texts.append(text)
    
    return {"text": texts}

# 데이터셋 준비 (예시 데이터)
MY_DATASET = [
    [
        {"from": "human", "value": "수학 문제를 풀어줄래? x^2 + 5x + 6 = 0의 해는?"},
        {"from": "gpt", "value": "<thought>\n이 문제는 이차방정식을 풀어야 합니다. x^2 + 5x + 6 = 0의 해를 구하기 위해 인수분해를 사용할 수 있습니다.\n\nx^2 + 5x + 6 = 0\n(x + a)(x + b) = 0 형태로 나타내려면 a + b = 5이고 a * b = 6을 만족해야 합니다.\n\na = 2, b = 3이면 a + b = 5이고 a * b = 6이므로 적합합니다.\n\n따라서 x^2 + 5x + 6 = (x + 2)(x + 3) = 0\n\n이 방정식의 해는 x + 2 = 0 또는 x + 3 = 0\nx = -2 또는 x = -3\n</thought>\n\n이 이차방정식을 풀기 위해 인수분해를 사용하겠습니다.\n\nx^2 + 5x + 6 = 0\n\n이 식을 (x + p)(x + q) 형태로 인수분해하려면, p + q = 5이고 p × q = 6을 만족하는 두 수 p, q를 찾아야 합니다.\n\np = 2, q = 3이면 두 조건을 모두 만족합니다.\n\n따라서 x^2 + 5x + 6 = (x + 2)(x + 3) = 0\n\n이 방정식의 해는:\nx + 2 = 0 또는 x + 3 = 0\nx = -2 또는 x = -3\n\n따라서 주어진 이차방정식의 해는 x = -2 또는 x = -3입니다."}
    ],
    # 더 많은 대화 예시 추가
]

# 데이터셋 변환
MY_DATASET = Dataset.from_dict({'conversations': MY_DATASET})
MY_DATASET = MY_DATASET.map(formatting_prompts_func, batched=True)

# 학습 설정
training_args = TrainingArguments(
    output_dir="outputs_exaone_deep",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    warmup_steps=10,
    num_train_epochs=2,
    learning_rate=2e-4,
    fp16=False,
    bf16=True,  # bfloat16 사용
    logging_steps=5,
    optim="paged_adamw_32bit",
    weight_decay=0.01,
    lr_scheduler_type="constant",
    seed=3407,
    max_grad_norm=0.3,
    group_by_length=True
)

# 트레이너 설정
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=MY_DATASET,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    dataset_num_proc=2,
    packing=False,
    args=training_args
)

# 학습 실행
trainer_stats = trainer.train()

# 모델 저장
model.save_pretrained("exaone_deep_finetuned")
tokenizer.save_pretrained("exaone_deep_finetuned")

# 추론 코드 (학습 후)
def inference():
    # 기본 모델 로드
    base_model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto"
    )
    
    # LoRA 어댑터 로드
    from peft import PeftModel
    model = PeftModel.from_pretrained(base_model, "exaone_deep_finetuned")
    tokenizer = AutoTokenizer.from_pretrained("exaone_deep_finetuned", trust_remote_code=True)
    
    # 추론 예시
    prompt = "x^2 - 4 = 0의 해는?"
    messages = [{"role": "user", "content": prompt}]
    input_ids = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt"
    )
    
    # 생성
    from transformers import TextIteratorStreamer
    from threading import Thread
    
    streamer = TextIteratorStreamer(tokenizer)
    thread = Thread(target=model.generate, kwargs=dict(
        input_ids=input_ids.to("cuda"),
        eos_token_id=tokenizer.eos_token_id,
        max_new_tokens=1024,
        do_sample=True,
        temperature=0.6,
        top_p=0.95,
        streamer=streamer
    ))
    thread.start()
    
    # 결과 출력
    for text in streamer:
        print(text, end="", flush=True)

# 필요시 추론 실행
# inference()
