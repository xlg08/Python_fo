import re

result = re.match(r'^1[3-9]\d{9}', "13345678921")
if result:
    print(result.group())