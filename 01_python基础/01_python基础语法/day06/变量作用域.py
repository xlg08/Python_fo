print("不可变类型")
"""
    数值型、布尔型
    字符串
    元组
"""
num = 0  # 数值型

print("1", num, id(num))  # 等


def _(x):
    print("3", x, id(x))  # 等
    x = 10  # 数值型

    print("4", x, id(x))  # 不等


print("2", num, id(num))  # 等
_(num)
print("5", num, id(num))  # 等

print("-" * 30)

str = "1 2 3 4 5 6"  # 字符型
print("1", str, id(str))  # 等


def _(x):
    print("3", x, id(x))  # 等
    x = x.replace("3", "7")
    print("4", x, id(x))  # 不等


print("2", str, id(str))  # 等
_(str)
print("5", str, id(str))  # 等

print("可变类型变量")
"""
    列表  list1 = []   或者  list1 = list()
    集合  set1 = {此时必须有值}     或者 set1 = set()
    字典  dict1 = {此时可以无值}    或者 dict1 = dict()
    
"""
print("=" * 30)

# 可变类型
# list1 = [1,2,3]
#
#
# print("1",list1,id(list1))
# def _(x):
#     print("3",x,id(x))
#     x.append(4)
#
#     print("4",x,id(x))
#
# print("2",list1,id(list1))
# _(list1)
# print("5",list1,id(list1))

print("♥" * 30)

# list1 = [1, 2, 3]
#
# print("1", list1, id(list1))
#
#
# def _(x):
#     print("3", x, id(x))
#     x.append({25, 8, 5, 6, 7, 2, 3})
#
#     print("4", x, id(x))
#
#
# print("2", list1, id(list1))
# _(list1)
# print("5", list1, id(list1))
