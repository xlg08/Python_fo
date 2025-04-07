"""
    del 列表[] : 删除列表中的某个元素
    pop(index) : 删除指定下标的数据(默认为最后一个)，并返回该数据
    remove()  :  移除列表中某个数据的第一个匹配项

"""
list1 = ["韦小宝", "张三", "李四", "王五"]
list2 = ["王五"]

# pop() 有返回值，返回值为删除的数据
print(list1.pop(1))



# list1.insert(0, "李四")
# # remove() 没有返回值
# print(list1)
# list1.remove("李四")
# print(list1)

list1.insert(0, "李四")
print(list1)
list3 = ["李四"]
# list1.remove(list3)     # 只有列表整体作为一个元素在另一个列表中才能删除
print(list1)



