"""
    append() :  增加指定数据到列表中
    extend() :  列表结尾追加数据，如果数据是一个序列，则将这个序列的数据注意添加到列表
    insert() :  指定位置新增数据

    在原列表里面追加了指定数据，即修改了原列表，故列表是一个可变序列
"""

list1 = ["韦小宝", "张三", "李四", "王五"]
list2 = ["王五"]

# 格式 ：列表名.append()      ，该方法没有返回值，要看列表内容，必须要打印列表
#  特点是默认末尾增加

# insert(): 指定位置新增数据
#   insert(index，value)      # 在index索引值的前面增加数据，index默认为

# list1.insert(2, "abc")
list1.insert(-2, "abc")     # 如果是负数则最后一个元素的索引为-1开始，向前
print(list1)


# extend() 列表结尾追加数据，如果数据是一个序列，则将该序列的数据注意添加到列表
# append()方法 实现 将一个新列表直接当作一个元素直接添加到另一个列表中，实现列表的嵌套。
# extend()方法 实现 将一个新序列中的每一个数据加入到另一个列表中。

# list2.extend(list1)
# 等价于
# list3 = list2 + list1
# print(list3)
# list3 = list1 - list2
# print(list3)
