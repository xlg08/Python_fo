"""
    lambda表达式称之为匿名函数(没有名字的函数)，简化python代码
    基本语法：
        lamdba 函数参数：表达式或者返回值

"""
def func():
    return 10


# 如何修改lambda表达式
funb = lambda : 10
print(funb)
print(funb())

print((lambda : 10)())

list1 = []
list1.sort()


students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

# # 按name值升序排列
# def i(x):
#     return x["age"]
#
# for _ in students:
#     print(i(_))


# students.sort(key=lambda dt: dt['name'])
students.sort(key=lambda dt: dt['name'])
# students.sort()
print(students)

list1 = [1, 2, 0, 5]
list1.sort()
print(list1)

# dt={{"name": "zhangsan"} {"name": "liis"}}
# list2 = [{"name": "zhangsan"}, {"name": "liis"}]
# print(list2)
# list2.sort()
# print(list2)
"""
    sort()方法语法：
        sort(key=None, reverse=False)
    参数
        sort()：接受两个仅限以关键字形式传入的参数 (仅限关键字参数)，

        这两个参数是可选的：
        key：指定带有一个参数的函数，用于从每个列表元素中提取比较键 (例如：key=str.lower)。
            对应于列表中每一项的键会被计算一次，然后在整个排序过程中使用。
            默认值 None 表示直接对列表项排序而不计算一个单独的键值。

        reverse：排序规则，为一个布尔值。
            reverse = True 降序， reverse = False 升序（默认）。

    返回值
        该方法没有返回值，但是会对列表的对象进行排序。

"""

# list.append()


