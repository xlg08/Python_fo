import random
"""
    1.定义一个字符串，如str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。
    编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码。
"""
print("第一题：")
str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print("长度：", len(str1))
num = ""
for i in range(4):
    a = random.randint(0, len(str1)-1)
    num += str1[a]
print(f"生成的验证码为：{num}")


"""
    2.已知列表 list1 = [11, 22, 33, 22, 11, 55], 
        请对其进行去重, 并将去重后的结果打印到控制台上.
"""
print("第二题：")
list1 = [11, 22, 33, 22, 11, 55]
for i in list1:
    a = list1.index(i)
    list1.remove(i)
    if i in list1:
        # print(f"{i}重复了")
        # print(list1)
        pass
    else:
        list1.insert(a, i)
else:
    print(f"去重后的列表为：{list1}")


"""
    3.键盘录入1个字符串并接收, 计算其中每个字符出现的次数, 并将结果打印到控制台上.
        例如:
            录入: abcbcAABBB11133
            输出: a(1)b(2)c(2)A(2)B(3)1(3)3(2)	格式一致即可, 不要求顺序.
"""
print("第三题：")
str3 = input("请输入一个字符串：\n")
# str3 = "abcbcAABBB11133"
dict3 = {}
result = ""

for i in str3:
    if i in dict3:  # 直接判断键是否存在
        dict3[i] += 1
    else:
        dict3[i] = 1

for k, v in dict3.items():
    result += f"{k}({v})"
print(result)


"""
    4给定一个集合numbers，集合中包含1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15元素，
        求该集合中所有奇数的和是多少.
"""
print("第四题：")
set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
sum = 0
for i in set4:
    if i % 2 != 0: sum += i
print(f"集合中所有奇数的和为：{sum}")







