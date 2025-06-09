import re, json, itertools

def extract_classes_by_name(text: str):
    pattern = r'Device\s+(\w+)\s*:\s*\n\s+"""(.*?)"""'
    matches = re.finditer(pattern, text, re.DOTALL)
    return {match.group(1): match.group(0) for match in matches}

with open("./ServiceExtraction/integration/service_list_ver1.1.8.txt", "r") as f:
    service_doc = f.read()
classes = extract_classes_by_name(service_doc)

extras = ["Wall", "SectorA", "SectorB", "Upper", "Lower", "Even", "Odd"]

tag1 = ["SectorA", "SectorB"]
tag2 = ["Upper", "Lower", "Wall"]
tag3 = ["Even", "Odd"]

combinations = list(itertools.product(tag1, tag2, tag3))

ret = {}
for class_name, class_doc in classes.items():
    for comb in combinations:
        dev_name = f"virtual_{class_name.lower()}_{comb}"
        dev_ret = {}
        dev_ret["id"] = dev_name
        dev_ret["category"] = class_name
        dev_ret["tags"] = [class_name] + list(comb)
        ret[dev_name] = dev_ret
print(len(ret))
json.dump(ret, open("service_list.json", "w"), ensure_ascii=False, indent=4)