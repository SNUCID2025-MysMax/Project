import os
from FlagEmbedding import BGEM3FlagModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# # 모델 저장 경로 설정

# # 디렉토리 생성
# os.makedirs(model_dir, exist_ok=True)

# from huggingface_hub import snapshot_download

# # 모델이 없는 경우에만 다운로드
# if not os.path.exists(os.path.join(model_dir, "config.json")):
#     print(f"모델을 다운로드합니다: {model_dir}")
#     # huggingface_hub를 사용하여 모델 다운로드
#     snapshot_download(
#         repo_id="BAAI/bge-m3",
#         local_dir=model_dir,
#         local_dir_use_symlinks=False  # 실제 파일 다운로드
#     )
#     print(f"모델이 성공적으로 다운로드되었습니다: {model_dir}")
# else:
#     print(f"이미 다운로드된 모델이 있습니다: {model_dir}")
