import requests

def deepl_translate(command, source="KO", target="EN", auth_key="6bc9c430-2abd-4f64-9f0d-09f6ac92441f:fx"):
    url = "https://api-free.deepl.com/v2/translate"
    data = {
        "auth_key": auth_key,
        "text": command,
        "source_lang": source,
        "target_lang": target,
    }

    try:
        response = requests.post(url, data=data, timeout=10)
        if response.status_code == 200:
            return response.json()['translations'][0]['text']
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        return command  # 실패 시 원문 유지
