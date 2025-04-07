# 变量的本质就是容器，可以变化的容器，在代码中存储数据
# 一个临时存储数据的容器


#数据类型分类的原因是为了精细化管理


#字符串中使用 """ """  特殊含义：保留字符串最原始的样子,不改变原格式

# 关键字：被开发者已经使用，并且赋予特殊含义的字

# 变量名可以使用中文，但是不推荐。

print("hello world")


x = 0


if x == 0 or x == 3 and x == 4:
    print("哈哈 ")
else:
    print("lala")

name = "张三"

age = 14

_________________ = ''

print(name, age, _________________)

name = "'张三'+'里斯'"
name2 = '"张三""里斯"'

print(name)
print(name2)

'''

    name = ""李四"+"李四""
    name = ''张三'+'李四''

'''


print('''
白日依山尽，
黄河入海流。
''')

print("""
白日依山尽，
黄河入海流。

""")


help('keyword')


# type方法可以查看变量类型
# 列表
list1 = [1, 2, 3]
print(type(list1))

tuple1 = (1, 2, 3)
print(type(tuple1))














