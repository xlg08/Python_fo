"""
    由于元组中的数据不允许直接修改，所以其操作方法大部分为查询方法。

        元组[索引]  :   根据'索引下标'查找元素
        index() :   查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index方法相同
        count() :   统计某个数据在当前元组出现的次数
        len()   :   统计元组中数据的个数

"""

tuple = (1, 1.5, "str", True, "str", "", " ")
# value：需要查找的值      start：从该索引开始查找(包括该索引)        stop：查找到该索引结束(不包括该索引)
print(tuple.index(1, 3, 4))  # True 的底层是1
# print(tuple.index(True, 0, -1))

print(tuple.count("str"))

print(len(tuple))

i = True + 2
print("打印：", i)

# 键不可重复，值可以重复但只会保留最后一个
