import yaml

lst = list(range(0, 12)) + [13]
for i in lst:
    print(f"Processing category {i}...")
    with open(f"./Testset/TestsetWithDevices_translated_no_seperation/category_{i}.yaml", "r") as file:
        d = yaml.safe_load(file)
    # print(d)
    for idx, item in enumerate(d):
        if len(item["code"])>1:
            print(f"{i}-{idx}")