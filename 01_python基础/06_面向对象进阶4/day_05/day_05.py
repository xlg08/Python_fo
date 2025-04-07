# 1. 生成批次歌词数据.
from math import ceil
import re

def dataset_loader(batch_size):

    # 读取文件
    with open("geci.txt", "r", encoding="utf-8") as src_f:
        lines = src_f.readlines()

        total_batch = ceil(len(lines) / batch_size)

        for idx in range(total_batch):
            yield lines[idx*batch_size:idx*batch_size+batch_size]

d1 =dataset_loader(8)
for temp_batch in d1:
    print(temp_batch)

# 2. 正则的几个案例.
# ①需求：在列表中["apple", "banana", "orange", "pear"]，匹配apple和pear
print("第一小题：")
list1 = ["apple", "banana", "orange", "pear"]
for value in list1:
    result = re.match("apple|pear", value)
    # 判断匹配是否成功
    if result:
        print("我想吃的水果：", result.group())
    else:
        print(f"我不想吃的水果：{value}")

# ②需求：匹配出163、126、qq等邮箱
print("第二小题：")
email = "45ax_cdsa@163.com"
result = re.match(r"^\w{6,18}@(163|126|qq)\.com$", email)
if result:
    print(result.group())
else:
    print("匹配失败")

# ③需求 :  匹配qq:10567这样的数据，提取出来qq文字和qq号码
print("第三小题：")
ee = "qq:10567"
result = re.match(r"^(qq):([1-9]\d{4,10})$", ee)

if result:
    print(result.group())
else:
    print("匹配失败")

# ④需求：匹配出<html>hh</html>
print("第四小题：")
html_s = "<html>hh</html>"
result = re.match(r"<([a-zA-Z]{1,4})>.*</\1>", html_s)
if result:
    print(result.group())
else:
    print("匹配失败")
# ⑤需求：匹配出<html><h1>www.itcast.cn</h1></html>
print("第五小题：")
html_s = "<html><h1>www.itcast.cn</h1></html>"
result = re.match(r"<([a-zA-Z]{1,4})><(h[1-6])>.*</\2></\1>", html_s)
if result:
    print(result.group())
else:
    print("匹配失败")