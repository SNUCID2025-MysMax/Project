import yaml, json
import time
from tqdm import tqdm
from FlagEmbedding import BGEM3FlagModel
from embedding_v1 import hybrid_recommend_v1
from embedding_v2 import hybrid_recommend_v2
from embedding_v3 import hybrid_recommend_v3
from embedding_v4 import hybrid_recommend_v4

result = []
model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)


version = "v4"

if version == "test":
    command = "Sound the alarm's siren if the barometric pressure is above 1020 hPa."
    recommended_items = hybrid_recommend_v4(
        model=model,
        query=command,
        max_k=20,
    )
    print(command)
    print([rec['key'] for rec in recommended_items])
# V1 - KOREAN
elif version == "v1":

    for i in range(0, 17):
        file_name = f"../Testset/TestsetWithDevices_translated/category_{i}.yaml"
        print(f"Processing file: {file_name}")

        with open(file_name, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        
        for item in tqdm(data):
            command = item["command"]
            devices = item["devices"]
            
            # 하이브리드 추천 모델 호출
            start_time = time.time()
            recommended_items = hybrid_recommend_v1(
                model=model,
                query=command,
            )
            end_time = time.time()
            extracted_devices = [rec['key'] for rec in recommended_items]
            
            ret = []
            for device in devices:
                if device not in extracted_devices and device != 'Clock':
                    ret.append(device)
            if ret:
                print(f"Missing devices for command '{command}': {ret}")
                result.append((f"category_{i}", command, ret,))

    with open("./embedding_result_v1.json", "w") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

elif version == "v2":

    # V2 - ENGLISH

    for i in range(2,3):
        file_name = f"../Testset/TestsetWithDevices_translated/category_{i}.yaml"
        print(f"Processing file: {file_name}")

        with open(file_name, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        
        for item in tqdm(data):
            command = item["command_translated"]
            devices = item["devices"]
            
            # 하이브리드 추천 모델 호출
            start_time = time.time()
            recommended_items = hybrid_recommend_v2(
                model=model,
                query=command,
            )
            end_time = time.time()
            extracted_devices = [rec['key'] for rec in recommended_items]
            
            ret = []
            for device in devices:
                if device not in extracted_devices:
                    ret.append(device)
            if ret:
                print(f"Missing devices for command '{command}': {ret}")
                result.append((f"category_{i}", command, ret,))

elif version == "v3":

    # V3 - Device
    def debug_device_scores(model, query, target_device):
        """특정 기기의 점수 확인"""
        # 전체 기기 점수 계산
        all_results = hybrid_recommend_v3(model, query, top_k=50)
        
        # 타겟 기기 찾기
        target_result = None
        for i, result in enumerate(all_results):
            if result['key'] == target_device:
                target_result = result
                rank = i + 1
                break
        
        if target_result:
            print(f"{target_device} found at rank {rank}")
            print(f"Score: {target_result['combined_score']:.4f}")
        else:
            print(f"{target_device} not found in top 50")

    for i in range(2,3):
        file_name = f"../Testset/TestsetWithDevices_translated/category_{i}.yaml"
        print(f"Processing file: {file_name}")

        with open(file_name, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        
        for item in tqdm(data):
            command = item["command_translated"]
            devices = item["devices"]
            
            # 하이브리드 추천 모델 호출
            start_time = time.time()
            recommended_items = hybrid_recommend_v3(
                model=model,
                query=command,
            )
            end_time = time.time()
            extracted_devices = [rec['key'] for rec in recommended_items]
            
            ret = []
            for device in devices:
                if device not in extracted_devices:
                    ret.append(device)
            if ret:
                print(f"Missing for '{command}': {ret}")
                for i in ret:
                    debug_device_scores(model, command, i)
                
                # print(f'Extracted: {extracted_devices}')
                # result.append((f"category_{i}", command, ret,))

elif version == "v4":
    for i in range(0, 17):
        file_name = f"../Testset/TestsetWithDevices_translated/category_{i}.yaml"
        print(f"Processing file: {file_name}")

        with open(file_name, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        
        for item in data:
            command = item["command_translated"]
            devices = item["devices"]
            
            # 하이브리드 추천 모델 호출
            start_time = time.time()
            recommended_items = hybrid_recommend_v4(
                model=model,
                query=command,
            )
            end_time = time.time()
            extracted_devices = [rec['key'] for rec in recommended_items]
            
            ret = []
            for device in devices:
                if device not in extracted_devices and device != 'Clock' and device != 'Speaker':
                    ret.append(device)
            if ret:
                print(f"Missing devices for command '{command}': {ret}")
                result.append((f"category_{i}", command, ret,))

    with open("./embedding_result_v4.json", "w") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)


# with open("./embedding_result_v4.json", "r") as f:
#     result = json.load(f)
# for category, command, missing_devices in result:
#     recommended_items = hybrid_recommend_v4(
#         model=model,
#         query=command,
#     )
#     print("f"Category: {category}, Command: {command}")"