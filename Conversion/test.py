from conversion import transform_code
import json
c = """class Scenario1:
    def __init__(self):
        self.cron = "0 20 1 1 1"  # 1월 1일 월요일 20:00에 시작
        self.period = 1000  # 1초마다 상태 확인
        self.var1 = "closed"  # 이전 상태
        self.var2 = 0         # 열린 횟수
        self.var3 = False     # 알람 울렸는지 여부

    def run(self):
        current = Tags("ContactSensor").contactSensor_contact

        if not self.var3 and self.var1 == "closed" and current == "open":
            self.var2 += 1
            if self.var2 == 2:
                All(Tags("Alarm").alarm_siren())
                self.var3 = True

        self.var1 = current
"""
print(json.dumps(transform_code(c), indent=2, ensure_ascii=False).replace("\\n","\n"))