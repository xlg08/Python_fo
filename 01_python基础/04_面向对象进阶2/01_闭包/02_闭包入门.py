"""
    闭包：
        概述：内部函数使用外部函数的变量，称之为闭包
        格式：
            def 外部函数(形参列表):
                外部函数(局部)变量
                def 内部函数(形参列表):
                    使用外部函数的变量
                return 内部函数名
                ！！！ 注意这里不要括号
    总结：闭包前提
        1.有嵌套
        2.有引用
        3.有返回

    闭包的作用：保存函数中的变量（外部函数中的变量）


"""

"""
    定义一个用于求和的闭包。
        其中，外部函数有参数num1，内部函数有参数num2，然后调用，并用于求解两数之和，观察效果。
"""


# 细节：1.函数名 和 函数名()  不是一个概念，前者是表示 函数对象(函数变量) 后者表示函数调用后的返回值
# 定义一个函数  函数名 函数名()
def get_sum(a, b):
    return a + b


print(get_sum)  # 函数对象
print(get_sum(10, 50))  # 此处函数调用，有返回值 60

# 既然是变量，则函数名可以赋值给一个变量，这就是函数对象
# 函数名 get_sum
# 赋值给一个变量 my_sum
my_sum = get_sum
# my_sum是一个函数对象、函数变量
print(my_sum)
print(my_sum(100, 300))

print("*" * 50)


# 闭包的构成条件:
# 1.外部函数
def func_out(num1):

    def func_inner(num2):  # 有嵌套
        nonlocal num1
        # 2内部函数
        num1 = num1 + num2  # 有引用
        print("求和：", num1)

    # 3外部函数返回了内部函数
    # 将内部函数作为一个整体进行返回
    return func_inner  # 有返回


# 调用函数
f = func_out(10)
# print(id(func_out(10)))
# print(id(func_out(10)))
# print(id(f))
# 执行闭包
f(1)
f(1)
f(1)
