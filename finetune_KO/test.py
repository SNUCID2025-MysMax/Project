import os
import glob
import importlib.util
import re

# 변수 로드 함수
def load_variable_from_pyfile(filepath, var_name):
    spec = importlib.util.spec_from_file_location("module.name", filepath)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return getattr(foo, var_name)

# 영어 문장만 추출해서 글자수 합산
def count_translation_chars(data):
    total_chars = 0
    for dialogue in data:
        for msg in dialogue:
            if msg["from"] == "human":
                match = re.search(r"Input: (.*?)\n\nServices:", msg["value"], re.DOTALL)
                if match:
                    english_input = match.group(1).strip()
                    if re.search(r"[a-zA-Z]", english_input):
                        total_chars += len(english_input)
    return total_chars

# 경로 설정
input_dir = "./finetune"
results = []

# data_*.py 파일 처리
for filepath in sorted(glob.glob(os.path.join(input_dir, "data_*.py"))):
    filename = os.path.basename(filepath)
    var_name = filename.replace(".py", "")

    try:
        data = load_variable_from_pyfile(filepath, var_name)
        dialogue_count = len(data)
        char_count = count_translation_chars(data)
        results.append((filename, dialogue_count, char_count))
    except Exception as e:
        results.append((filename, "❌", f"오류: {e}"))

# 출력
print("\n📊 각 파일별 대화 세트 수 + 번역 글자 수:")
print("-" * 60)
print(f"{'파일명':<20} {'세트 수':<10} {'번역 글자 수':<15}")
print("-" * 60)
for fname, count, chars in results:
    print(f"{fname:<20} {count:<10} {chars:<15}")
