import json

def print_json_pretty_with_real_newlines(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ 입력 파일 읽는 중 오류 발생: {e}")
        return

    try:
        json_str = json.dumps(data, indent=4, ensure_ascii=False)
        # json.dumps는 문자열 내 줄바꿈을 \\n으로 만듦 → \n으로 복원
        json_str = json_str.replace('\\n', '\n')

        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.write(json_str)
    except Exception as e:
        print(f"❌ 출력 파일 저장 중 오류 발생: {e}")

if __name__ == "__main__":
    NUM_CATEGORY = 16
    for ctg_num in range(NUM_CATEGORY):
        input_path = f"TestCase\\category_{ctg_num}.json"
        output_path = f"TestCase\\category_{ctg_num}.txt"
        print_json_pretty_with_real_newlines(input_path, output_path)

