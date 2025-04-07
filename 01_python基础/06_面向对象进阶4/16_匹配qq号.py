# 需求 是 匹配QQ号
# 数字 qq:10567

import re

ee = "qq:1245664"
result = re.match(r"^(qq):([1-9]\d{4,10})$", ee)

if result:
    print(result.group())
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))
else:
    print("匹配失败")
