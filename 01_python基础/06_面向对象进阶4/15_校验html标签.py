"""
    正则校验：


"""
import re

# 需求: 匹配出 <html> hh </html>

# html_s = "<html>hh</html>"


html_s = "<html><h1>hh</h1></html>"

# 演示分组
# result = re.match(r"<html><h1>.*</h1></html>", html_s)
result = re.match(r"<([a-zA-Z]{1,4})><(h[1-6])>.*</\2></\1>", html_s)

# result = re.match(r"<(?P<A>[a-zA-Z]{1,4})><(?P<B>h[1-6])>.*</(?P=B)></(?P=A)>", html_s)

# 引入分组概念
if result:
    print(result.group())
    # print(result.group(0))
    # print(result.group(1))
    # print(result.group(2))
else:
    print("匹配失败")