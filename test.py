# print("Hello, World!")

import re

code = """(#Device1 #Device2).function
# info0
(#Device2  #Device3).function # info1
# info2
# info3 (#Device3 #Dv3).function2
# sdf
(#Dev2)"""

# 정규식으로 "# "로 시작하는 주석 제거
cleaned_code = '\n'.join([re.sub(r'#\s.*', '', line).rstrip() for line in code.splitlines()])
for line in cleaned_code.splitlines():
    print("|",line)
