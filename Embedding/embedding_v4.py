import os
import numpy as np
import json
import pickle
import re
from sklearn.metrics.pairwise import cosine_similarity
from FlagEmbedding import BGEM3FlagModel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 데이터 로드
dense_embeddings = np.load(os.path.join(BASE_DIR, 'embedding_result_v4', 'dense_embeddings.npy'))

with open(os.path.join(BASE_DIR, 'embedding_result_v4', 'colbert_embeddings.pkl'), 'rb') as f:
    colbert_embeddings = pickle.load(f)

with open(os.path.join(BASE_DIR, 'embedding_result_v4', 'sparse_embeddings.json')) as f:
    sparse_embeddings = json.load(f)

with open(os.path.join(BASE_DIR, 'embedding_result_v4', 'metadata.json')) as f:
    metadata = json.load(f)

# 카멜 케이스 분리 함수
def split_camel_case(identifier):
    """카멜 케이스를 단어별로 분리"""
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    result = [m.group(0) for m in matches]
    if not result or (len(result) == 1 and result[0] == identifier):
        return [identifier]
    return result

# 디바이스가 쿼리에 포함되어 있는지 확인
def device_in_query(device_name, query, debug=False):
    """디바이스 이름이 쿼리에 포함되어 있는지 확인 (단어 경계 기반, 복수형 포함)"""
    # 카멜 케이스 분리하고 공백으로 연결, 소문자 변환
    parts = split_camel_case(device_name)
    device_str = ' '.join(parts).lower()
    query_lower = query.lower()
    
    if debug:
        print(f"검사 중: '{device_name}' -> parts: {parts} -> device_str: '{device_str}'")

    # 단어 경계를 사용한 정확한 매칭
    patterns = [
        # 단수형 정확한 매칭
        f'\\b{re.escape(device_str)}\\b',
        # 복수형 s
        f'\\b{re.escape(device_str)}s\\b',
        # 복수형 es
        f'\\b{re.escape(device_str)}es\\b'
    ]
    
    # 패턴 중 하나라도 매칭되면 True
    for i, pattern in enumerate(patterns):
        if re.search(pattern, query_lower):
            if debug:
                pattern_type = ["단수형", "복수형(s)", "복수형(es)"][i]
                print(f"  -> ✓ {pattern_type} 매칭: '{pattern}'")
            return True
    
    if debug:
        print(f"  -> ✗ 매칭 없음")
    return False

# 우선순위 적용 함수
def prioritize_devices_in_results(results, query, max_k=10):
    """쿼리에 언급된 디바이스를 우선순위로 배치하고, 나머지는 점수순 정렬 후 max_k개 반환"""
    prioritized = []
    others = []

    # 우선순위 디바이스와 일반 디바이스 분리
    for r in results:
        if device_in_query(r['key'], query):
            prioritized.append(r)
        else:
            others.append(r)

    # 우선순위 디바이스들을 점수 순으로 정렬 (높은 점수부터)
    prioritized.sort(key=lambda x: x['combined_score'], reverse=True)
    
    # 나머지 디바이스들도 점수 순으로 정렬 (높은 점수부터)
    others.sort(key=lambda x: x['combined_score'], reverse=True)

    # 우선순위 디바이스를 앞에, 나머지를 뒤에 배치하고 max_k개만 반환
    final_results = prioritized + others
    return final_results[:max_k]

# ColBERT 유사도 계산 함수
def colbert_softmax_maxsim(query_vec, doc_vecs, temperature=0.05):
    sim_matrix = cosine_similarity(query_vec, doc_vecs)
    max_sim = np.max(sim_matrix, axis=1)
    weights = np.exp(max_sim / temperature)
    weights /= np.sum(weights)
    return np.sum(weights * max_sim)

# 하이브리드 추천 함수 (우선순위 적용)
def hybrid_recommend_v4(model, query, devices_available=None, top_k=10, max_k=10, weights=(0.6, 0.3, 0.1)):
    query_emb = model.encode(
        [query], 
        return_dense=True,
        return_sparse=True,
        return_colbert_vecs=True
    )
    
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
    
    max_score = max(dense_scores.max(), 1e-6)
    combined_scores = (
        weights[0] * dense_scores/max_score +
        weights[1] * np.array(sparse_scores) +
        weights[2] * np.array(colbert_scores)
    )

    sorted_indices = np.argsort(combined_scores)[::-1]

    if devices_available is not None:
        available_set = set(d.lower() for d in devices_available)
        sorted_indices = [i for i in sorted_indices if metadata['keys'][i].lower() in available_set]

    top_indices = sorted_indices

    # 기본 결과 생성
    results = [{
        'key': metadata['keys'][i],
        'text': metadata['texts'][i],
        'dense_score': float(dense_scores[i]),
        'sparse_score': float(sparse_scores[i]),
        'colbert_score': float(colbert_scores[i]),
        'combined_score': float(combined_scores[i])
    } for i in top_indices]
    
    # 우선순위 적용 및 max_k개 반환
    prioritized_results = prioritize_devices_in_results(results, query, max_k)
    
    return prioritized_results

# 사용 예시
if __name__ == "__main__":
    model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)
    
    
    # 테스트 쿼리
    query = 'If the fans in Sector B and Sector A are both on, close one of the odd-tagged blinds.'
    results = hybrid_recommend_v4(model, query, max_k=10)
    
    print(f"Query: {query}")
    print("Results with priority:")
    for i, result in enumerate(results):
        device_mentioned = device_in_query(result['key'], query, debug=True)
        priority_mark = "★" if device_mentioned else " "
        print(f"{priority_mark} {i+1}. {result['key']} (Score: {result['combined_score']:.4f})")
        print()  # 디버깅 출력과 구분하기 위한 빈 줄