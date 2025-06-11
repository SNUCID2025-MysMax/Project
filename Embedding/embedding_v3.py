import os
import numpy as np
import json
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from FlagEmbedding import BGEM3FlagModel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 데이터 로드
dense_embeddings = np.load(os.path.join(BASE_DIR, 'embedding_result_v3', 'dense_embeddings.npy'))

with open(os.path.join(BASE_DIR, 'embedding_result_v3', 'colbert_embeddings.pkl'), 'rb') as f:
    colbert_embeddings = pickle.load(f)

with open(os.path.join(BASE_DIR, 'embedding_result_v3', 'sparse_embeddings.json')) as f:
    sparse_embeddings = json.load(f)

with open(os.path.join(BASE_DIR, 'embedding_result_v3', 'metadata.json')) as f:
    metadata = json.load(f)

with open(os.path.join(BASE_DIR, 'embedding_result_v3', 'device_index_mapping.json')) as f:
    device_index_mapping = json.load(f)

# ColBERT 유사도 계산 함수
def colbert_softmax_maxsim(query_vec, doc_vecs, temperature=0.05):
    sim_matrix = cosine_similarity(query_vec, doc_vecs)
    max_sim = np.max(sim_matrix, axis=1)
    weights = np.exp(max_sim / temperature)
    weights /= np.sum(weights)
    return np.sum(weights * max_sim)

def hybrid_recommend_v3(model, query, devices_available=None, top_k=10, weights=(0.6, 0.3, 0.1)):
    """계층적 검색 기반 하이브리드 추천"""
    
    # 1. 쿼리 임베딩 생성
    query_emb = model.encode(
        [query],
        return_dense=True,
        return_sparse=True,
        return_colbert_vecs=True
    )
    
    # 2. 전체 점수 계산
    dense_scores = cosine_similarity([query_emb['dense_vecs'][0]], dense_embeddings)[0]
    
    sparse_scores = []
    query_weights = query_emb['lexical_weights'][0]
    for doc_weights in sparse_embeddings:
        score = sum(query_weights.get(token, 0) * doc_weights.get(token, 0) for token in query_weights)
        sparse_scores.append(score)
    
    colbert_scores = [
        colbert_softmax_maxsim(query_emb['colbert_vecs'][0], doc_emb)
        for doc_emb in colbert_embeddings
    ]
    
    # 3. devices_available 필터링
    available_devices = device_index_mapping.keys()
    if devices_available is not None:
        available_set = set(d.lower() for d in devices_available)
        available_devices = [d for d in device_index_mapping.keys() if d.lower() in available_set]
    
    # 4. 기기별 계층적 점수 계산
    device_scores = {}
    
    for device_type in available_devices:
        indices = device_index_mapping[device_type]
        
        if not indices:
            continue
        
        # 해당 기기의 각 점수 추출
        device_dense = [dense_scores[idx] for idx in indices]
        device_sparse = [sparse_scores[idx] for idx in indices]
        device_colbert = [colbert_scores[idx] for idx in indices]
        
        # 상위 5개 점수만 사용 (편향 제거)
        top_5_dense = sorted(device_dense, reverse=True)[:5]
        top_5_sparse = sorted(device_sparse, reverse=True)[:5]
        top_5_colbert = sorted(device_colbert, reverse=True)[:5]
        
        # 가중 평균 계산 (상위 점수에 더 높은 가중치)
        def weighted_average(scores):
            if not scores:
                return 0.0
            score_weights = [1.0, 0.8, 0.6, 0.4, 0.2][:len(scores)]
            weighted_sum = sum(s * w for s, w in zip(scores, score_weights))
            weight_sum = sum(score_weights)
            return weighted_sum / weight_sum
        
        avg_dense = weighted_average(top_5_dense)
        avg_sparse = weighted_average(top_5_sparse)
        avg_colbert = weighted_average(top_5_colbert)
        
        # 정규화 (dense 점수 정규화)
        max_dense = max(dense_scores.max(), 1e-6)
        normalized_dense = avg_dense / max_dense
        
        # 최종 점수 계산
        final_score = (
            weights[0] * normalized_dense +
            weights[1] * avg_sparse +
            weights[2] * avg_colbert
        )
        
        # 일관성 보너스 (높은 점수가 여러 개 있을 때)
        high_score_count = len([s for s in top_5_dense + top_5_sparse + top_5_colbert if s > 0.7])
        consistency_bonus = 1.0 + (high_score_count * 0.02)  # 최대 30% 보너스
        
        final_score *= consistency_bonus
        
        # 최고 점수 표현 찾기
        combined_device_scores = [
            weights[0] * (dense_scores[idx] / max_dense) + 
            weights[1] * sparse_scores[idx] + 
            weights[2] * colbert_scores[idx]
            for idx in indices
        ]
        best_idx = indices[np.argmax(combined_device_scores)]
        best_expression = metadata['metadata'][best_idx]['expression']
        max_individual = max(combined_device_scores)
        
        device_scores[device_type] = {
            'final_score': final_score,
            'avg_dense': avg_dense,
            'avg_sparse': avg_sparse,
            'avg_colbert': avg_colbert,
            'best_expression': best_expression,
            'max_individual_score': max_individual,
            'expression_count': len(indices)
        }
    
    # 5. 점수로 정렬하고 상위 top_k개 무조건 반환
    sorted_devices = sorted(device_scores.items(), key=lambda x: x[1]['final_score'], reverse=True)
    
    # 6. 상위 top_k개 무조건 반환 (필터링 제거)
    top_devices = sorted_devices[:top_k]
    
    # 7. 결과 포맷팅
    return format_hierarchical_results(top_devices)


def format_hierarchical_results(filtered_devices):
    """계층적 검색 결과 포맷팅"""
    results = []
    for device_type, scores in filtered_devices:
        results.append({
            'key': device_type,
            'text': scores['best_expression'],
            'dense_score': float(scores['avg_dense']),
            'sparse_score': float(scores['avg_sparse']),
            'colbert_score': float(scores['avg_colbert']),
            'combined_score': float(scores['final_score']),
            'expression_count': scores['expression_count'],
            'max_individual_score': float(scores['max_individual_score'])
        })
    return results

# 사용 예시
if __name__ == "__main__":
    model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)
    
    # 테스트 쿼리
    query = "turn on the air conditioner"
    results = hybrid_recommend_v3(model, query, top_k=5)
    
    print(f"Query: {query}")
    print("Hierarchical Results:")
    for i, result in enumerate(results):
        print(f"{i+1}. Device: {result['key']}")
        print(f"   Expression: {result['text']}")
        print(f"   Final Score: {result['combined_score']:.4f}")
        print(f"   Expression Count: {result['expression_count']}")
        print()
