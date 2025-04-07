import re

email = "axcdsa@163.com"

# 校验邮箱合法
# result = re.match(r"^[a-zA-Z_0-9]{6,18}@(163|126|qq)\.com$", email)

# 等价于
result = re.match(r"^\w{6,18}@(163|126|qq)\.com$", email)

if result:
    print(result.group())
    print(result.group(0))  # 获取第0组信息，效果同上，即：整个匹配到的结果是0组
    print(result.group(1))  # 从左往右数，第几个左小括号，就表示第一组
else:
    print("匹配失败")


