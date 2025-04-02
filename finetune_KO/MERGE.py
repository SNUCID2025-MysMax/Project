from peft import PeftModel

# base model 불러오기
from transformers import AutoModelForCausalLM

base_model = AutoModelForCausalLM.from_pretrained(
    "LGAI-EXAONE/EXAONE-Deep-7.8B",
    trust_remote_code=True,
    torch_dtype="auto",
    device_map=None
)

# LoRA 적용 모델 불러오기
model = PeftModel.from_pretrained(base_model, "lora_exaone_adapter")

# 🔁 Merge: LoRA 가중치를 base model에 통합
model = model.merge_and_unload()

model.save_pretrained("merged_exaone")