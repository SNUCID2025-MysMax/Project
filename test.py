# # print("Hello, World!")
# s = """
# [{'name': 'AlarmOnWindowMultipleOpenClosed', 'cron': '', 'period': 1000, 'code': 'open_timestamp := 0\nopen_count := 0\nwindow_opened := false\nalarm_triggered := false\ncurrent_state = (#Window).windowControl_window\ncurrent_time = (#Clock).clock_timestamp\nif ((current_state == "open") and (window_opened == false)) {\n    window_opened = true\n    open_timestamp = current_time\n    open_count = open_count + 1\n}\nif ((current_state == "closed") and (window_opened == true)) {\n    window_opened = false\n    if ((open_count >= 3) and ((current_time - open_timestamp) > 1800000) and (alarm_triggered == false)) {\n        alarm_triggered = true\n        if (any(#Alarm)) {\n            all(#Alarm).alarm_siren()\n        } else if (any(#Siren)) {\n            all(#Siren).sirenMode_setSirenMode("siren")\n        }\n    }\n}\nif (current_state == "closed" and open_count < 3) {\n    alarm_triggered = false\n}'}]
# """
# print(s)

# "//" 뒤 주석 제거 (C/C++/Java 스타일)
import re
script = """
//This is a code
1+2 // This is a comment
// 3+2
//dfs
4+5
"""
script = '\n'.join([re.sub(r'//.*', '', line).rstrip() for line in script.splitlines()])
print(script)