import json

def print_json_pretty_with_real_newlines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        print(f"\ncommand: {item['command']}")
        print(f"\npython:\n{item['python']}")

        print("\ncode:")
        for code_block in item['code']:
            print(f"  name: {code_block['name']}")
            print(f"  cron: {code_block['cron']}")
            print(f"  period: {code_block['period']}")
            print(f"  code:\n{code_block['code']}")
        print("\n" + "=" * 80)

file_path = 'category_1.json' 
print_json_pretty_with_real_newlines(file_path)

