"""

    定义一个既能装饰减法运算，又能装饰加法运算的装饰器，即带有参数的装饰器。


    记忆：
        1(规定).1个装饰器的参数有且只能有1个
        2.如果装饰器有多个参数，可以在该装饰器外面在包裹一层装饰器，把该装饰器当作内部函数即可

"""

# 装饰器
def my_sum_sub(fn_name):
    def fn_inner(a, b):
        print("正在计算")
        return fn_name(a, b)
    return fn_inner

# 原函数
@my_sum_sub
def get_sum(a, b):
    return a + b

@my_sum_sub
def get_sub(a, b):
    return a - b

if __name__ == '__main__':
    print(get_sum(10, 20))
    print(get_sub(10, 20))



