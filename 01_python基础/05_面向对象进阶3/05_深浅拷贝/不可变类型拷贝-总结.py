import copy
"""
    深拷贝时针对于不可变类型容器:
        其内部元素如果都是不可变类型，则与普通赋值相同
        其内部元素如果存在可变类型元素，则不可变类型容器会拷贝成一个对象，其内部的可变类型元素也会拷贝成一个新的对象
    深拷贝时针对于不可变类型容器:
        与普通赋值相同
"""

a = [11, 22]

e = (a,)
b = (1, 2, 3, 4, e, 6)
# c = b
c = copy.deepcopy(b)

print("a的id：", id(a))
print("b的id：", id(b))       # 与c的地址值不同
print("b[4]:", id(b[4]))
print(b)

print("c的id：", id(c))       # 与b的地址值不同
print("c[4]的id：", id(c[4]))
print(c)

b[4][0][0] = 0
print("改变后：")
print("b的id：", id(b))
print("b[4]的id：", id(b[4]))
print(b)

print("c的id：", id(c))
print("c[4]的id：", id(c[4]))
print(c)

# 深拷贝：不可变类型
#   其内部元素是不可变类型时，与普通赋值相同
# a = (11, 22)
#
# b = (1, 2, 3, 4, a, 6)
# # c = a
# c = copy.deepcopy(b)
# # c = copy.copy(a)
# print("b的id：", id(b))
# print("b[4]:", id(b[4]))
# print(b)
#
# print("c的id：", id(c))
# print("c[4]的id：", id(c[4]))
# print(c)
#
# # b[4][0] = 0         # 不可变类型不能被修改，会报错
# print("改变后：")
# print("b的id：", id(b))
# print("b[4]的id：", id(b[4]))
# print(b)
#
# print("c的id：", id(c))
# print("c[4]的id：", id(c[4]))
# print(c)


# 不可变类型的浅拷贝
#     无论内部元素是可变类型还是不可变类型
# 针对于不可变类型，浅拷贝和普通赋值相同，内部的地址都是不会改变的
# a = [11, 22]
#
#
# b = (1, 2, 3, 4, a, 6)
#
# c = copy.copy(b)
#
# print("b的id：", id(b))
# print("b[4]:", id(b[4]))
# print(b)
#
# print("c的id：", id(c))
# print("c[4]的id：", id(c[4]))
# print(c)
#
# b[4][0] = 0
# print("改变后：")
# print("b的id：", id(b))
# print("b[4]的id：", id(b[4]))
# print(b)
#
# print("c的id：", id(c))
# print("c[4]的id：", id(c[4]))
# print(c)

# 普通赋值
# a = [11, 22]
#
# b = (1, 2, 3, 4, a, 6)
# c = b
#
#
# print("b的id：", id(b))
# print("b[4]:", id(b[4]))
# print(b)
#
# print("c的id：", id(c))
# print("c[4]的id：", id(c[4]))
# print(c)
#
# b[4][0] = 0
# print("改变后：")
# print("b的id：", id(b))
# print("b[4]的id：", id(b[4]))
# print(b)
#
# print("c的id：", id(c))
# print("c[4]的id：", id(c[4]))
# print(c)
