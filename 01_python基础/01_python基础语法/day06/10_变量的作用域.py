"""

    作用域：类似于势力范围
    局部变量与全局变量
    全局变量：在整个程序范围内都可以使用
    局部变量：在函数的调用过程中，开始定义。。。。

    为了要在局部作用域下修改全局变量，引入了 global

    global 代表声明为全局变量（此刻起使用的就是这个全局变量）

"""

# num = 20
# def snum():
#     # global num        # 使用了global关键字，将局部变量提升为全局变量
#     # num = 50
#     print(num)
#     函数体内部就是局部作用域
#
# snum()
# # print(num)


def num():
    global x        # 此处也可以是没在全局作用域中定义，只在局部作用域中定义的变量
    x = 10
num()
print(x)
