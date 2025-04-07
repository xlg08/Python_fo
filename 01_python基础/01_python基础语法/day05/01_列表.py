"""
    列表  list
    通过一个变量保存多条数据，首选list

    list的基本语法：
        列表变量名称 = [数据1, 数据2, 数据3, ... ]

"""

# 提示：
    # 1.变量名不能是关键字
    # 2.列表里面的数据和数据之间是逗号(英文)

list1 = [""]
print(type(list1))
print(id(list1))

# 列表的访问  列表名[索引值]
list2 = ["张三", "李四", "王五", "啦啦啦"]
list3 = [2, 1.0, True, list2]
print(list3[3][3])
print(list3[3][3][2])

# 新的列表
list4 = list2 + ['d']
print(list4)


