import json

def print_json_pretty_with_real_newlines(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ 입력 파일 읽는 중 오류 발생: {e}")
        return

    try:
        with open(output_path, 'w', encoding='utf-8') as f_out:
            for item in data:
                f_out.write(f"\ncommand: {item['command']}")
                f_out.write(f"\npython:\n{item['python']}")

                f_out.write("\ncode:")
                for code_block in item['code']:
                    f_out.write(f"  name: {code_block['name']}")
                    f_out.write(f"  cron: {code_block['cron']}")
                    f_out.write(f"  period: {code_block['period']}")
                    f_out.write(f"  code:\n{code_block['code']}")
                f_out.write("\n" + "=" * 80)
    except Exception as e:
        print(f"❌ 출력 파일 저장 중 오류 발생: {e}")

if __name__ == "__main__":
    NUM_CATEGORY = 16
    for ctg_num in range(NUM_CATEGORY):
        input_path = f"TestCase\\category_{ctg_num}.json"
        output_path = f"TestCase\\category_{ctg_num}.txt"
        print_json_pretty_with_real_newlines(input_path, output_path)

