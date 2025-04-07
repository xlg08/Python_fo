"""

    列表[索引] = 修改后的值   :   修改列表中的某个元素
    reverse()              :  将数据序列进行倒叙排列
    sort()                 :   对列表序列进行排序    默认从小到大排序

"""

# reverse()方法 没有返回值


# sort()方法 没有返回值
list1 = [45, 55, 655, 52, 1154, 2, 5, 7]
list1.sort()
list1.sort(reverse=True)
print(list1)

