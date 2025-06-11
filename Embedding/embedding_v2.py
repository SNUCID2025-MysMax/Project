import os
import numpy as np
import json
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from FlagEmbedding import BGEM3FlagModel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 데이터 로드
dense_embeddings = np.load(os.path.join(BASE_DIR, 'embedding_result_v2', 'dense_embeddings.npy'))

with open(os.path.join(BASE_DIR, 'embedding_result_v2', 'colbert_embeddings.pkl'), 'rb') as f:
    colbert_embeddings = pickle.load(f)

with open(os.path.join(BASE_DIR, 'embedding_result_v2', 'sparse_embeddings.json')) as f:
    sparse_embeddings = json.load(f)

with open(os.path.join(BASE_DIR, 'embedding_result_v2', 'metadata.json')) as f:
    metadata = json.load(f)

# ColBERT 유사도 계산 함수
def colbert_softmax_maxsim(query_vec, doc_vecs, temperature=0.05):
    sim_matrix = cosine_similarity(query_vec, doc_vecs)
    max_sim = np.max(sim_matrix, axis=1)
    weights = np.exp(max_sim / temperature)
    weights /= np.sum(weights)
    return np.sum(weights * max_sim)

# 중복 디바이스 제거 함수
def filter_unique_devices(sorted_indices, all_metadata, top_k=10):
    """동일 device_type 중복 제거하여 첫 번째만 포함"""
    seen_devices = set()
    filtered = []
    for idx in sorted_indices:
        device_type = all_metadata[idx]['device_type']
        if device_type not in seen_devices:
            filtered.append(idx)
            seen_devices.add(device_type)
        if len(filtered) >= top_k:
            break
    return filtered

# 수정된 하이브리드 추천 함수
def hybrid_recommend_v2(model, query, devices_available=None, top_k=10, max_k=10, weights=(0.6, 0.3, 0.1)):
    query_emb = model.encode(
        [query], 
        return_dense=True,
        return_sparse=True,
        return_colbert_vecs=True
    )
    
    # Dense 점수 계산
    dense_scores = cosine_similarity([query_emb['dense_vecs'][0]], dense_embeddings)[0]

    # Sparse 점수 계산
    sparse_scores = []
    query_weights = query_emb['lexical_weights'][0]
    for doc_weights in sparse_embeddings:
        score = sum(query_weights.get(token, 0) * doc_weights.get(token, 0) for token in query_weights)
        sparse_scores.append(score)
    
    # ColBERT 점수 계산
    colbert_scores = [
        colbert_softmax_maxsim(query_emb['colbert_vecs'][0], doc_emb)
        for doc_emb in colbert_embeddings
    ]
    
    # 점수 정규화 및 결합
    max_score = max(dense_scores.max(), 1e-6)
    combined_scores = (
        weights[0] * dense_scores/max_score +
        weights[1] * np.array(sparse_scores) +
        weights[2] * np.array(colbert_scores)
    )

    # 점수순 정렬
    sorted_indices = np.argsort(combined_scores)[::-1]

    # devices_available 필터링 (기존 방식 유지하되 metadata 구조 변경 반영)
    if devices_available is not None:
        available_set = set(d.lower() for d in devices_available)
        sorted_indices = [i for i in sorted_indices if metadata['metadata'][i]['device_type'].lower() in available_set]

    # 중복 device_type 제거
    filtered_indices = filter_unique_devices(sorted_indices, metadata['metadata'], max_k)

    # 점수 차이 및 max_k 제한 적용
    gap_threshold = 0.01
    initial_top = 5
    top_indices = []
    
    for i, idx in enumerate(filtered_indices):
        if len(top_indices) >= max_k:
            break
        if i == 0:
            top_indices.append(idx)
            continue
        prev = combined_scores[top_indices[-1]]
        curr = combined_scores[idx]
        if curr >= 0.5 or abs(prev - curr) <= gap_threshold or len(top_indices) < initial_top:
            top_indices.append(idx)
        else:
            break

    # 결과 반환 (metadata 구조 변경 반영)
    return [{
        'key': metadata['metadata'][i]['device_type'],
        'text': metadata['metadata'][i]['expression'],
        'dense_score': float(dense_scores[i]),
        'sparse_score': float(sparse_scores[i]),
        'colbert_score': float(colbert_scores[i]),
        'combined_score': float(combined_scores[i])
    } for i in top_indices]

# 사용 예시
if __name__ == "__main__":
    model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)
    
    # 테스트 쿼리
    query = "turn on the air conditioner"
    results = hybrid_recommend_v2(model, query, top_k=5)
    
    print(f"Query: {query}")
    print("Results:")
    for i, result in enumerate(results):
        print(f"{i+1}. Device: {result['key']}")
        print(f"   Expression: {result['text']}")
        print(f"   Combined Score: {result['combined_score']:.4f}")
        print()
