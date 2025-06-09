import re,json,os

import yaml
from yaml.representer import SafeRepresenter

class LiteralString(str):
    pass

def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

yaml.add_representer(LiteralString, literal_str_representer)

class QuotedString(str):
    pass

def quoted_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

yaml.add_representer(QuotedString, quoted_str_representer)

def remove_line_comment(line: str) -> str:
    # //로 시작하는 주석 제거 (줄 끝 주석 포함)
    return re.sub(r'\s*//.*$', '', line).rstrip()

def parse_scenarios_with_command(script: str):
    raw_lines = part.strip().splitlines()
    lines = [remove_line_comment(line) for line in raw_lines if remove_line_comment(line).strip()]

    command = lines[0].replace("\",,","").replace("\"","")
    script = "\n".join(lines[1:]).strip()
    parts = [part.strip() for part in script.strip().split('---') if part.strip()]
    scenarios = []

    num = 1
    for part in parts:
        lines = part.strip().splitlines()
        name = lines[0].split('=', 1)[1].strip().strip('"')
        cron = lines[1].split('=', 1)[1].strip().strip('"')
        period = int(lines[2].split('=', 1)[1].strip())
        code = "\n".join(lines[3:]).strip() + "\n"  # 줄바꿈 포함시켜 | 출력 유도

        scenarios.append({
            # "name": QuotedString(name),
            "name": QuotedString(f'Scenario{num}'),
            "cron": QuotedString(cron),
            "period": period,
            "code": LiteralString(code)
        })
        num += 1

    return {
      "command": QuotedString(command),
      "code": scenarios
      }

def parse_scenarios(script: str):
    parts = [part.strip() for part in script.strip().split('---') if part.strip()]
    scenarios = []

    for part in parts:
        raw_lines = part.strip().splitlines()
        lines = [remove_line_comment(line) for line in raw_lines if remove_line_comment(line).strip()]

        name = lines[0].split('=', 1)[1].strip().strip('"')
        cron = lines[1].split('=', 1)[1].strip().strip('"')
        period = int(lines[2].split('=', 1)[1].strip())
        code = "\n".join(lines[3:]).strip() + "\n"  # 줄바꿈 포함시켜 | 출력 유도

        scenarios.append({
            "name": QuotedString(name),
            "cron": QuotedString(cron),
            "period": period,
            "code": LiteralString(code)
        })

    return {
      "code": scenarios
    }

def extract_last_code_block(text):
  pattern = r"```(?:[^\n]*)\n(.*?)```"
  matches = re.findall(pattern, text, re.DOTALL)
  return matches[-1].strip() if matches else None

if __name__ == "__main__":
    script = """
    name = "Scenario1"
    cron = "0 9 * * 1-5"
    period = 0
    if (((#Window).contactContactSensor_contact == 'closed') and (#AirQualityDetector).carbonDioxideMeasurement_carbonDioxide >= 1000 and (#AirQualityDetector).temperatureMeasurement_temperature >= 30.0) {
      (#Clock).clock_delay(0, 0, 5)
      (#Window).windowControl_open()
      if ((#Fan).switch_switch == 'off' ) {
        (#Fan).switch_on()
      }
    }
    ---
    name = "Scenario2"
    cron = ""
    period = 100
    count := 0
    if ((#AirQualityDetector).dustSensor_fineDustLevel >= 50) {
      count = count + 1
    } else {
      count = 0
      }
    if (count >= 60) {
      (#Window).windowControl_close()
      (#Fan).switch_off()
      if ((#HumiditySensor).relativeHumidityMeasurement_humidity <= 40.0){
        (#Humidifier).switch_on()
      }
      if ((#SoilMoistureSensor).soilHumidityMeasurement_soilHumidity <= 25.0 and (#Irrigator).switch_switch == 'off') {
        (#Irrigator).switch_on()
      }
    }
    """
    
    print(parse_scenarios(extract_last_code_block(script)))