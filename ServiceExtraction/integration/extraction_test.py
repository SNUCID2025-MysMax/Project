import re

with open("service_list_ver1.1.8.txt", "r") as f:
    service_doc = f.read()

def extract_classes_by_name(text: str):
    # pattern = r'class\s+(\w+)\s*:\s*\n\s+"""(.*?)"""'
    pattern = r'Device\s+(\w+)\s*:\s*\n\s+"""(.*?)"""'
    matches = re.finditer(pattern, text, re.DOTALL)

    class_dict = {}
    for match in matches:
        class_name = match.group(1)
        full_class_def = match.group(0)  # 전체 클래스 문자열
        class_dict[class_name] = full_class_def

    return class_dict

classes = extract_classes_by_name(service_doc)

dsl_text = classes["AirPurifier"]

def extract_accessors(dsl_text: str):
    block_patterns = {
        "Tags": re.compile(r"Tags:\n((?:\s+#[^\n]*\n)+)"),
        # "Enums": re.compile(r"Enums:\n((?:\s+\w+: \[[^\]]+\]\n*)+)"),
        "Attributes": re.compile(r"Attributes:\n((?:\s+\w+_\w+: [^\n]+\n*)+)"),
        "Methods": re.compile(r"Methods:\n((?:\s+\w+\([^\)]*\) -> \w+[^\n]*\n*)+)")
    }

    # Apply all patterns to the sample DSL text
    blocks = {
        name: (pattern.search(dsl_text).group(1).strip()).split("\n    ")
        for name, pattern in block_patterns.items()
        if pattern.search(dsl_text)
    }

    if blocks.get("Attributes"):
        blocks["Attributes"] = [line.split(":")[0].strip() for line in blocks.get("Attributes", [])]
    if blocks.get("Methods"):
        blocks["Methods"] = [line.split("(")[0].strip() for line in blocks.get("Methods", [])]
    return blocks

classes = {device:extract_accessors(classes[device]) for device in classes.keys()}
print(classes["AirPurifier"])
