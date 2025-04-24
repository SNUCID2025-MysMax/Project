import numpy as np
import json, pickle
from sklearn.metrics.pairwise import cosine_similarity
from FlagEmbedding import BGEM3FlagModel

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # ChatGPT 디렉토리 경로
dense_path = os.path.join(BASE_DIR, 'embedding_result', 'dense_embeddings.npy')
dense_embeddings = np.load(dense_path)

# 모델 및 데이터 초기화
model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=False)  # CPU 환경

# 임베딩 데이터 로드 (ColBERT 추가)
dense_embeddings = np.load('./embedding_result/dense_embeddings.npy')
# colbert_data = np.load('./embedding_result/colbert_embeddings.npz', allow_pickle=True)
# colbert_embeddings = [emb.astype(np.float32) for emb in colbert_data['colbert']]  # float32로 변환
with open('./embedding_result/colbert_embeddings.pkl', 'rb') as f:
    colbert_embeddings = pickle.load(f)

with open('./embedding_result/sparse_embeddings.json') as f:
    sparse_embeddings = json.load(f)
    
with open('./embedding_result/metadata.json') as f:
    metadata = json.load(f)

# ColBERT 유사도 계산 함수
# 1) 평균 맥스심 점수
def colbert_maxsim(query_vec, doc_vecs):
    """
    query_vec: [query_tokens, dim]
    doc_vecs: [doc_tokens, dim]
    """
    sim_matrix = cosine_similarity(query_vec, doc_vecs)
    return np.max(sim_matrix, axis=1).mean()  

# 2) Softmax MaxSim
def colbert_softmax_maxsim(query_vec, doc_vecs, temperature=0.05):
    sim_matrix = cosine_similarity(query_vec, doc_vecs)
    max_sim = np.max(sim_matrix, axis=1)
    weights = np.exp(max_sim / temperature)
    weights /= np.sum(weights)
    return np.sum(weights * max_sim)

# 하이브리드 추천 함수
def hybrid_recommend(query, top_k=10, max_k=15, weights=(0.6, 0.3, 0.1)):
    # 쿼리 임베딩 생성
    query_emb = model.encode(
        [query], 
        return_dense=True,
        return_sparse=True,
        return_colbert_vecs=True
    )
    
    # 각 유사도 계산
    dense_scores = cosine_similarity([query_emb['dense_vecs'][0]], dense_embeddings)[0]
    
    sparse_scores = []
    query_weights = query_emb['lexical_weights'][0]  # dict

    for doc_weights in sparse_embeddings:  # 문서별 sparse dict
        score = sum(query_weights.get(token, 0) * doc_weights.get(token, 0) for token in query_weights)
        sparse_scores.append(score)
    
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
    
    # # 상위 K개 추출
    # top_indices = np.argsort(combined_scores)[-top_k:][::-1]

    # 유사 결과 많을 경우 확장
    sorted_indices = np.argsort(combined_scores)[::-1]

    gap_threshold = 0.01
    initial_top = 5
    top_indices = [sorted_indices[0]]

    for i in range(1, len(sorted_indices)):
        if len(top_indices) >= max_k:
            break
        prev = combined_scores[top_indices[-1]]
        curr = combined_scores[sorted_indices[i]]
        if curr >= 0.5 or abs(prev - curr) <= gap_threshold or len(top_indices) < initial_top:
            top_indices.append(sorted_indices[i])
        else:
            break

    return [{
        'key': metadata['keys'][i],
        'text': metadata['texts'][i],
        'dense_score': float(dense_scores[i]),
        'sparse_score': float(sparse_scores[i]),
        'colbert_score': float(colbert_scores[i]),
        'combined_score': float(combined_scores[i])
    } for i in top_indices]


# # 추천 실행
# results = hybrid_recommend(
#     "날씨가 맑고, 기온이 30도 이상이면 커튼을 닫고 에어컨을 틀고, 미세먼지가 나쁘면 창문을 닫고 공기청정기를 켜줘.", 
#     top_k=10)

# # 결과 출력
# print("추천 서비스:")
# for idx, item in enumerate(results, 1):
#     print(f"{idx}. {item['key']}")
#     print(f"   종합 점수: {item['combined_score']:.4f}")
#     print(f"   Dense: {item['dense_score']:.3f}, Sparse: {item['sparse_score']:.3f}, ColBERT: {item['colbert_score']:.3f}")
