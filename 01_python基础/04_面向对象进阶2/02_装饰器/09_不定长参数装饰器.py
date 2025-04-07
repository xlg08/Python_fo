#   定义一个可以计算多个数据和多个字典value值之和的函数，并调用。
#   在原有函数的计算结果之前，加一个友好提示(不能改变源码)：正在努力计算中...。

# 2.装饰器
def my_sum(fn_name):
    def fn_inner(*args, **Kwargs):
        print("正在努力计算中。。")
        return fn_name(*args, **Kwargs)
    return fn_inner

# @my_sum
# 1.原函数
def get_sum(*args, **Kwargs):
    # # *args  数据元组
    # # **Kwargs
    # # 定义求和计数器
    # sum = 0
    #
    # # 遍历获取元组中的值
    # for i in args:
    #     sum += i
    #
    # for v in Kwargs.values():
    #     sum += v
    #
    # return sum
    return sum(args) + sum(Kwargs.values())


if __name__ == '__main__':

    # 魔法方法
    # print(get_sum(1, 2, 3, a=4, b=5, c=6))

    # 传统方法
    get_sum = my_sum(get_sum)
    print(get_sum(1, 2, 3, a=4, b=5, c=6))