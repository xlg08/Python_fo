"""
    特点：
        __name__    get_sum

    巧用魔法方法 __namae__
    获取原函数原始名字   "进行字符串比较"
    if 原始名字 == "get_sum":
        加法
    elif 原始名字 == "get_sub":
        减法

"""

# 装饰器
def my_sum_sub(fn_name):
    def fn_inner(a, b):

        if fn_name.__name__ == "get_sum":
            print("正在努力计算加法。。")
        elif fn_name.__name__ == "get_sub":
            print("正在努力计算减法。。")

        return fn_name(a, b)
    return fn_inner




@my_sum_sub
# 原始方法
def get_sum(a, b):
    return a + b

@my_sum_sub
def get_sub(a, b):
    return a - b

if __name__ == '__main__':
    print(get_sum(10, 20))

