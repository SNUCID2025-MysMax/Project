import re
import json

def extract_classes_by_name(text: str):
    pattern = r'Device\s+(\w+)\s*:\s*\n\s+"""(.*?)"""'
    matches = re.finditer(pattern, text, re.DOTALL)
    return {match.group(1): match.group(0) for match in matches}

with open("../ServiceExtraction/integration/service_list_ver1.1.8.txt", "r") as f:
    service_doc = extract_classes_by_name(f.read())


things = {}
for key, value in service_doc.items():
    things[key] = {
        "id": key,
        "category": key,
        "tags": [key],
    }
with open("things.json", "w") as f:
    
    json.dump(things, f, indent=4, ensure_ascii=False)