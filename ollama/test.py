import ollama
import time
import pprint
from prompt_info import grammar, samples, description

def main():
    # models = ollama.list()
    # model = models.models[0].model
    # print([m.model for m in models.models], model)
    
    # model = "exaone-deep:7.8b"
    # model = "llama3.2:3B"
    # model = "codellama:7b"
    model = "qwen2.5-coder:7b"

    try:
        print("\n모델에 질문을 보냅니다...")
        start_time = time.time()

        prompt = f"""
You are a helpful assistant that generates SoPlang code for user_command based on the given grammar and samples.
----------------------------------------------------------------------
[Grammar]
grammar = {grammar},
[/Grammar]
----------------------------------------------------------------------
[Samples]
samples = {samples},
[/Samples]
----------------------------------------------------------------------
[Services]
services = {pprint.pformat(description)},
[/Services]
----------------------------------------------------------------------

Let's think step by step.

#Step1. You have to find the best solution for the user. If the command is too vague, you MUST find the best solution within a limited list of services

#Step2. generate SoPlang code for user_command based on given services.

#Step3. Check whether the code has appropriate, corrrect services and SoPlang grammar. If not, you MUST fix it.

PLEASE GENERATE SoPLANG CODE ONLY, NOT PYTHON CODE.
Do not give any other description.

user_command = "I'm too hot."
"""
                
        response = ollama.chat(
            model= model,
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            stream=True
        )

        full_response = ""
    
        # 스트리밍 응답 처리
        for chunk in response:
            if 'message' in chunk and 'content' in chunk['message']:
                content = chunk['message']['content']
                print(content, end='', flush=True)
                full_response += content
        
        end_time = time.time()
        
        print("\n=== 모델 응답 ===")
        # print(response['message']['content'])
        print("\n=== 응답 완료 ===")
        print(f"응답 시간: {end_time - start_time:.2f}초")
        
        # 추가 정보 출력
        if 'prompt_eval_count' in response:
            print(f"프롬프트 평가 토큰 수: {response['prompt_eval_count']}")
        if 'eval_count' in response:
            print(f"생성된 토큰 수: {response['eval_count']}")
        
    except Exception as e:
        print(f"모델 호출 중 오류 발생: {e}")

if __name__ == "__main__":
    main()
