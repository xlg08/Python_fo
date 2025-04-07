import copy
# 深浅拷贝主要是针对可变类型，
#         深拷贝拷贝所有（可变类型）的层
#         浅拷贝只拷贝（可变类型）的第一层
#     如果是针对于不可变类型，则用法和普通赋值一样。并无区别
a = [11,22]
b = (1,2,3,a)

c = copy.deepcopy(b)
print(id(b))
print(id(c))

# c = b

