import ollama
import time
import json
import pprint
from prompt_info import grammar, services

def load_test_cases(filename="test_cases.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def save_test_results(results, filename="test_results.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

def make_prompt(user_command):
    return f"""
You are a domain-specific language assistant specialized in generating SoPLang code based on user commands.

-------------------------------------------------------------------------------
[Grammar Specification]
Below is the complete SoPLang grammar definition. Use it as the only valid syntax reference.

grammar = {grammar}
[/Grammar Specification]
-------------------------------------------------------------------------------
[Device and Skills]
Below is the list of available devices, their skill functions, and value accessors.

Only use the device and their skills defined here. Select the most relevant action from this list.

devices and skills = {services}
[/Device and Skills]
-------------------------------------------------------------------------------

Your task consists of the following steps:

Step 1. Interpret the `user_command` and determine the best matching device, function, and parameters using ONLY the provided services.

Step 2. Generate a complete SoPLang script in correct syntax using the grammar definition.

Step 3. Validate that:
  - All device references (e.g., (#AirConditioner)) use the correct device and skill_function/value_id format.
  - The structure follows the grammar rules exactly.
  - All arguments are used properly.
If there is any mismatch, you MUST correct it before final output.

STRICT RULES:
- Only return SoPLang code as your final answer.
- Do NOT return Python code.
- Do NOT return any explanation, reasoning, or additional text.
- All device calls must follow this format: `(#DeviceName).skillId_functionId(arg)` or `(#DeviceName).skillId_valueId`

-------------------------------------------------------------------------------
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
