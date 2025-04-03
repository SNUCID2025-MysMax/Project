import ollama

from .device_mapping import google_translate,Device_Mapping
from .SERVICE_DESCRIPTION_FINAL import description
from .fix_code import fix_code2
from .code_prompt import grammar, samples

import time
def generate_code(sentence,needed_services):
    prompt = f"Grammar:{grammar}\n\n Samples:{samples}, Input: {sentence}\n\n services: {needed_services}"
    response = ollama.chat(model='soplang', messages=[
  {
    'role': 'user',
    'content':prompt
  },
])
    return response['message']['content']

def pipeline(sentence):
    total_start = time.perf_counter()
    start = time.perf_counter()

    english_sentence = google_translate(sentence)
    end = time.perf_counter()
    print(f"1. Google Translate Time: {end - start:.4f} seconds")
    print(english_sentence)

    start = end
    devices = Device_Mapping(english_sentence,str(description),model='soplang')
    end = time.perf_counter()
    print(f"2. Device Mapping Time: {end - start:.4f} seconds")
    print(devices)

    start = end
    needed_services = dict()
    for device in devices:
        needed_services[device] = description[device]
    code = generate_code(english_sentence,needed_services)
    end = time.perf_counter()
    print(f"3. Generate Code Time: {end - start:.4f} seconds")
    print(code)

    start = end
    code = fix_code2(code)
    end = time.perf_counter()
    print(f"4. Fix Code Time: {end - start:.4f} seconds")
    print(f"Final Total Speed: {end - total_start:.4f} seconds")
    print(code)

    return code


if __name__ == '__main__':
    dataset = ['1시간마다 TV mute 토글해줘',
    '화요일 목요일 금요일 오후 2시에 눈이오면 에어컨을 heat 모드로 틀어줘']
    for data in dataset:
        pipeline(data)
        
