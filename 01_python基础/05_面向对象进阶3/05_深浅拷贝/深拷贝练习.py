import copy

a = [11, 22]
b = (33, 44)

c = [1, 2, 3, a, 4]
d = (1, 2, 3, a, 4)
e = [1, 2, 3, b, 4]
f = (1, 2, 3, b, 4)

c1 = copy.deepcopy(c)

print("深拷贝下列表中套列表----可变类型中有可变类型")
print("c的id：", id(c))
print("c1的id：", id(c1))
print("*" * 35)
print("c[3]:", id(c[3]))
print("c1[3]的id：", id(c1[3]))
print("*" * 35)
print("不变c[0]:", id(c[0]))
print("不变c1[0]的id：", id(c1[0]))
print("*" * 35)
print("c与c1地址是否相同：", id(c) == id(c1))
print("c[3]与c1[3]地址是否相同：", id(c[3]) == id(c1[3]))
print("不变c[0]与c1[0]地址是否相同：", id(c[0]) == id(c1[0]))

print("\n")

d1 = copy.deepcopy(d)

print("深拷贝下元组中套列表----不可变类型中有可变类型")
print("d的id：", id(d))
print("d1的id：", id(d1))
print("*" * 35)
print("d[3]:", id(d[3]))
print("d1[3]的id：", id(d1[3]))
print("*" * 35)
print("d与d1地址是否相同：", id(d) == id(d1))
print("d[3]与d1[3]地址是否相同：", id(d[3]) == id(d1[3]))

print("\n")

e1 = copy.deepcopy(e)

print("深拷贝下列表中套元组----可变类型中有不可变类型")
print("e的id：", id(e))
print("e1的id：", id(e1))
print("*" * 35)
print("e[3]:", id(e[3]))
print("e1[3]的id：", id(e1[3]))
print("*" * 35)
print("e与e1地址是否相同：", id(e) == id(e1))
print("e[3]与e1[3]地址是否相同：", id(e[3]) == id(e1[3]))

print("\n")

f1 = copy.deepcopy(f)

print("深拷贝下元组中套元组----不可变类型中有不可变类型")
print("f的id：", id(f))
print("f1的id：", id(f1))
print("*" * 35)
print("f[3]:", id(f[3]))
print("f1[3]的id：", id(f1[3]))
print("*" * 35)
print("f与f1地址是否相同：", id(f) == id(f1))
print("f[3]与f1[3]地址是否相同：", id(f[3]) == id(f1[3]))