import time
# 简答题
"""
（1）闭包的特点是什么？
    用来延长函数内的变量的生命周期
    闭包可以保存函数内的变量，而不会随着调用完函数而被销毁。

    闭包的构成条件：
        ①有嵌套：在函数嵌套(函数里面再定义函数)的前提下；
        ②有引用：内部函数使用了外部函数的变量(还包括外部函数的参数)；
        ③有返回：外部函数返回了内部函数名。

"""

"""
（2）什么是装饰器？装饰器有哪些特点？
    装饰器：
    装饰器的作用是不改变原有函数的基础上，给原有函数增加额外功能。
    装饰器本质上就是一个闭包函数。
    
    装饰器： ①有嵌套：在函数嵌套(函数里面再定义函数)的前提下；
            ②有引用：内部函数使用了外部函数的变量(还包括外部函数的参数)；
            ③有返回：外部函数返回了内部函数名；
            ④有额外功能：给需要装饰的原有函数增加额外功能。
"""

"""
(4)复习可变参数与不可以参数内容
    不定长参数，也叫可变参数，用于不确定调用时会传递多少个参数场景(或者一个不传递)

    1.不定长位置参数 (不定长元组参数，可以使用一个元组来接受所有的参数)
        *args  *args参数整体   args变量名  *只是一个符号，没有别的意思
    2.不定长关键字参数 (不定长字典参数)，使用一个字典接受所有的参数
        **kargs  **kwargs 是一个整体    kwargs是一个变量名

    规则：
        1.两者可以单独使用
        2.也可以配合使用，但是*args要放在**kwargs前面。否则报错
        
    # 可变数据类型：内存地址一旦固定，其值可以发生改变，在赋值过程中，一个改变，另一个一定改变
        列表、集合、字典
    # 不可变数据类型：内存地址一旦固定，其值不可以发生改变，在赋值过程中，一个改变，另一个一定不改变
        数值型、布尔型、字符串、元组
    
"""

# 实操题

#（1）定义一个闭包，用于求解方程的y与x值的变化，例如 y = ax + b。
print("第一题：")
def linear_equation(a, b):
    def solve(**kwargs):
        x = kwargs.get('x')
        y = kwargs.get('y')
        if x is not None:
            return a * x + b
        elif y is not None:
            return (y - b) / a
    return solve

solver = linear_equation(2, 3)

print(f"当 x=5 时，y = {solver(x=5)}")
print(f"当 y=13 时，x = {solver(y=13)}")

"""
（2）创建一个闭包，实现统计函数执行的次数功能。有如下调用闭包函数的代码：
    ```python
    f = func_count()
    f()
    f()
    f()
    ```
    执行结果如下：
    > hello world
    > 执行了1次
    > hello world
    > 执行了2次
    > hello world
    > 执行了3次

    请完善 func_count 函数的实现。
"""

print("第二题：")
def func_count(f):
    count = 0
    def fn_inner():
        nonlocal count
        count += 1
        f()
        print(f"执行了{count}次")
    return fn_inner


def f():
    print("hello world")

f = func_count(f)
f()
f()
f()

#（3）请使用装饰器方式来统计输出100000句"程序员YYDS"的执行时间。
print("第三题：")
def calculation_time(yyds):
    def fn_inner():
        start_time = time.time()
        for i in range(100000):
            yyds()
        end_time = time.time()
        print()
        print(f"输出100000句\"程序员YYDS\"总共花费{end_time-start_time}s")
    return fn_inner

@calculation_time
def yyds():
    print("程序员YYDS", end="\t")

yyds()

#（4）定义一个函数, 返回字符串, 使用装饰器实现对这个字符串添加后缀.txt。
print("第四题：")
def add_suffix(str_s):
    def fn_inner():
        return str_s() + ".txt"
    return fn_inner

@add_suffix
def str_s():
    return "heima"


print(str_s())