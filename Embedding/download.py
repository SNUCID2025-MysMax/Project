from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="BAAI/bge-m3",
    local_dir="/home/ubuntu/Project/models/bge-m3",
    local_dir_use_symlinks=False  # 실제 파일 복사
)
