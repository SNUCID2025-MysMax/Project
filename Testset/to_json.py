raw_input = """<"섹터 에이에 있는 선풍기를 꺼 줘.">
class Scenario1:
    def __init__(self):
        self.cron = ""
        self.period = -1

    def run(self):
        Tags("sectorA", "Fan").switch_off()


<"섹터 비와 섹터 에이에 있는 선풍기가 모두 켜져 있으면 홀수 태그가 붙은 블라인드 중 하나를 닫아 줘.">
class Scenario1:
    def __init__(self):
        self.cron = ""
        self.period = -1

    def run(self):
        sectorA_on = Tags("sectorA", "Fan").switch_switch == "on"
        sectorB_on = Tags("sectorB", "Fan").switch_switch == "on"
        if (sectorA_on == True) and (sectorB_on == True):
            Tags("odd", "Blind").blind_close()
			

<"홀수 태그가 붙은 선풍기 중 하나라도 켜져 있으면, 하단부에 있는 모든 관개 장치를 꺼 줘.">
class Scenario1:
    def __init__(self):
        self.cron = ""
        self.period = -1

    def run(self):
        if Any(Tags("odd", "Fan").switch_switch == "on"):
            All(Tags("lower", "Irrigator").switch_off())


<"짝수 태그가 붙은 창문이 열려 있으면 섹터 에이에 있는 선풍기를 꺼 줘.">
class Scenario1:
    def __init__(self):
        self.cron = ""
        self.period = -1

    def run(self):
        if Tags("even", "Window").windowControl_window == "open":
            Tags("sectorA", "Fan").switch_off()


<"섹터 비에 있는 홀수 태그가 붙은 관개 장치를 모두 꺼 줘.">
class Scenario1:
    def __init__(self):
        self.cron = ""
        self.period = -1

    def run(self):
        All(Tags("sectorB", "odd", "Irrigator").switch_off())


<"상단부에 있는 짝수 태그가 붙은 창문이 열려 있으면 커튼을 닫아 줘.">
class Scenario1:
    def __init__(self):
        self.cron = ""
        self.period = -1

    def run(self):
        if Tags("upper", "even", "Window").windowControl_window == "open":
            Tags("Curtain").curtain_close()


<"상단부에 있는 조명이 모두 꺼져 있으면, 홀수 태그가 붙은 모든 창문을 열어 줘.">
class Scenario1:
    def __init__(self):
        self.cron = ""
        self.period = -1

    def run(self):
        if All(Tags("upper", "Light").switch_switch == "off"):
            All(Tags("odd", "Window").windowControl_open())


<"짝수 태그가 붙은 스피커 중 하나라도 켜져 있으면 섹터 비에 있는 조명을 모두 꺼 줘.">
class Scenario1:
    def __init__(self):
        self.cron = ""
        self.period = -1

    def run(self):
        if Any(Tags("even", "Speaker").switch_switch == "on"):
            All(Tags("sectorB", "Light").switch_off())


<"벽에 있는 홀수 태그가 붙은 모든 블라인드가 열려 있으면 조명을 꺼 줘.">
class Scenario1:
    def __init__(self):
        self.cron = ""
        self.period = -1

    def run(self):
        if All(Tags("wall", "odd", "Blind").blind_blind == "open"):
            Tags("Light").switch_off()


<"상단부에 있거나 섹터 에이에 있는 조명 중 하나가 켜져 있으면 선풍기를 모두 켜 줘.">
class Scenario1:
    def __init__(self):
        self.cron = ""
        self.period = -1

    def run(self):
        upper_on = Any(Tags("upper", "Light").switch_switch == "on")
        sectorA_on = Any(Tags("sectorA", "Light").switch_switch == "on")
        if (upper_on == True) or (sectorA_on == True):
            All(Tags("Fan").switch_on())
"""

import json
import re

def parse_command_code_blocks(text):
    # 정규식: <"명령어"> + 그 다음 class~부터 다음 <"시작 전까지 코드 블록 추출
    pattern = r'<"(.*?)">\s*\n(class Scenario1:.*?)(?=\n<"|$)'
    matches = re.findall(pattern, text, re.DOTALL)

    result = []
    for command, code in matches:
        code_fixed = code.replace('"', "'").replace("\\t","\t")
        result.append({
            "command": command.strip(),
            "python": f"```python\n{code_fixed.rstrip()}```"
        })
    return result


json_output = parse_command_code_blocks(raw_input)
with open("output.json", "w", encoding="utf-8") as f:
    f.write("[\n")
    for i, item in enumerate(json_output):
        f.write("  {\n")
        f.write(f"    \"command\": \"{item['command']}\",\n")
        # json.dumps로 다시 escape 안 되도록 직접 출력
        f.write(f"    \"python\": \"{json.dumps(item['python'])[1:-1]}\"\n")  # 따옴표 제거
        if i == len(json_output) - 1:
            f.write("  }\n")
        else:
            f.write("  },\n")
    f.write("]\n")
