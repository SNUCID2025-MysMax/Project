import ollama
import time
import json
import pprint
from prompt_info import grammar, samples, description

def load_test_cases(filename="test_cases.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def save_test_results(results, filename="test_results.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

def make_prompt(user_command):
    return f"""
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

user_command = "{user_command}"
"""

def run_test_case(model, user_command, use_stream=True):
    prompt = make_prompt(user_command)
    start_time = time.time()

    try:
        if use_stream:
            response = ollama.chat(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                stream=True
            )

            full_response = ""
            for chunk in response:
                if 'message' in chunk and 'content' in chunk['message']:
                    content = chunk['message']['content']
                    full_response += content

            elapsed = time.time() - start_time
            return full_response.strip(), round(elapsed, 2), None  # 토큰 수 없음 (stream 모드)

        else:
            response = ollama.chat(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )

            full_response = response['message']['content']
            elapsed = time.time() - start_time

            generated_tokens = response.get("eval_count", None)
            return full_response.strip(), round(elapsed, 2), generated_tokens

    except Exception as e:
        return f"Error: {e}", None, None

def main():
    model = "qwen2.5-coder:7b"
    test_cases = load_test_cases()
    test_results = []

    for idx, pair in enumerate(test_cases):
        human_input = pair[0]["value"].replace("Input: ", "")
        print(f"\n[{idx+1}/{len(test_cases)}] Testing: {human_input}")

        result, elapsed_time, generated_tokens = run_test_case(model, human_input, use_stream=use_stream)

        test_results.append([
            pair[0],
            pair[1],
            {
                "result": result,
                "elapsed_time": elapsed_time,
                "generated_tokens": generated_tokens
            }
        ])

    save_test_results(test_results)
    print("\n✅ All test cases completed and saved to test_results.json.")

if __name__ == "__main__":
    main()
