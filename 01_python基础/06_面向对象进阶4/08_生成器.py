"""
    生成器：
        基于数据规则，用一部分数据生成一部分数据，而不是一下子生成完所有
    目的：
        节省大量内存
    实现方式：
        1.推导式写
        2.yield 关键字     伪代码_思想

"""

# 1.推导式写
# 列表推导式
# my_generator = [i for i in range(1, 11)]
# 集合推导式
# my_generator = {i for i in range(1, 11)}        # <class 'set'>

# 返回生成器 不是 元组
# my_generator = (i for i in range(1, 11))        # <class 'generator'>
#
# print(type(my_generator))
#
#
# # 从生成器中获取数据     next()
# print(next(my_generator))
# print(next(my_generator))
#
# print("*"*30)
# for i in my_generator:
#     print(i, end="\t")

# 特点 ：内存空间占用 少


import sys
# 普通列表推导式
my_list = [i for i in range(1000000000)]
my_gt = (i for i in range(1000000000))

print()
# 使用系统方法来查看底层内存占用情况  拿这个数据在底层的存储空间
# 该方法用来返回对象的大小，以字节的形式，也就是该对象底层的内存空间大小
print(f"my_list在内存中占用：{sys.getsizeof(my_list)}")
print(f"my_gt在内存中占用：{sys.getsizeof(my_gt)}")
