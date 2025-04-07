# """
#     推导式：
#         while 循环  for循环    for ... if    for ... for  的简便写法
#
#     推导式语法：
#         [结果 for i in 数据容器]      简化for循环
#         [结果 for i in 数据容器 if 判断条件]      简化for循环+if结构
#         [结果 for i in 数据容器 for j in 数据容器]    简化for循环+for循环   i的为外循环 j为内循环
#
#
# """
#
# # for i in range(5):
# #     print(i)
# # 等价于
# # [print(i) for i in range(5)]
#
# dict1 = {
#     "name":"张三",
#     "age":18
# }
#
# # [print(f"{k} : {dict1[k]}") for k in dict1]
# [print(f"{k} : {dict1[k]}") for k in dict1 if k == "age"]
#
#
# # for i in range(5):
# #     for j in range (5):
# #         print(f"{i}+{j}")
# # 等价于
# # [print(f"{i}+{j}") for i in range(5) for j in range(5)]
#
# print(type(object))
# print(type(type))
#
# print(object.__base__)
# print(type.__base__)
#
# print(int.__base__)
# print(type(int))
#
# print(type.__class__)
# print(object.__class__)
# print(int.__class__)


# str = "itcase"
# list1 = list(str)
print(list("itcase"))

# print(list1)
#
# list2 = list()
# print(list2)

str1 = "asss"
def a():
    a = "asss"
    print(id(a))
str2 = 'asss'
i = 1
h = 2
j = 1
print(id(str1))
print(id(str2))
print(id(i))
print(id(j))
a()


# 集合要求其元素必须是不可变的（即可哈希的）,
#   因为字典是可变对象,所以集合（set）不能直接包含字典（dict），
# list1 = {[],[]}
# list1 = {{"name":"张三"},{"name":"李四"}}
# print(list1)

# tuple = ([],[])
# print(tuple)
# 元组（tuple）是不可变对象，因此它是可哈希的，可以作为集合的元素或字典的键。
#   然而，元组中可以包含可变对象（如字典、列表等），但这并不会影响元组本身的不可变性。
#   元组的不可变性是指元组的结构（即它包含的元素及其顺序）不可变，而不是它内部的元素不可变。

# list2 = ["张三","李四"]
# list3 = ["张三","李四"]
# list = (list2,list3)
# list2.append("王五")
# print(list)

"""
    在 Python 中，可哈希的（hashable） 是指一个对象在其生命周期内具有不变的哈希值
    （即可以通过 hash() 函数计算出一个固定值），
    并且可以与其他对象进行比较（通过 __eq__() 方法）。
    只有可哈希的对象才能作为字典的键或集合的元素。
    
    可哈希的条件
    一个对象是可哈希的，必须满足以下条件：
        哈希值不变：
            对象的哈希值在其生命周期内必须保持不变。
            哈希值是通过 hash() 函数计算的，通常用于快速查找和比较。
        支持相等比较：
            对象必须实现 __eq__() 方法，用于判断两个对象是否相等。
            如果两个对象相等，它们的哈希值也必须相等（即 a == b 必须满足 hash(a) == hash(b)）。
        不可变性（通常）：
            大多数情况下，不可变对象（如整数、字符串、元组等）是可哈希的。
            可变对象（如列表、字典、集合等）通常是不可哈希的，因为它们的内容可以改变，导致哈希值变化。
    
    一些常见的可哈希对象：
        不可变类型：
            整数（int）
            浮点数（float）
            字符串（str）
            布尔值（bool）
            元组（tuple，但要求元组内的所有元素也是可哈希的）
            冻结集合（frozenset）
        自定义对象：
            默认情况下，用户定义的类的实例是可哈希的，因为它们的哈希值基于对象的内存地址。
            如果自定义类实现了 __eq__() 方法，通常也需要实现 __hash__() 方法，以确保对象是可哈希的。
    一些常见的不可哈希的对象
        可变类型：
            列表（list）
            字典（dict）
            集合（set）
"""

