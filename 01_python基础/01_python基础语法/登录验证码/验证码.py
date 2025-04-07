import random

str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 随机数  randint(开始位置,结束位置)
# 拿字符串中字符  字符串名字[索引]
# len(str1)-1  索引的最大值= 长度-1
for i in range(4):
    print(str1[random.randint(0, len(str1) - 1)],end="")

# str2 = random.sample(str1,4)
# print("".join(str2))
