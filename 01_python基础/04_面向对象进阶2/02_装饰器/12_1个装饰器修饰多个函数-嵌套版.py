# 装饰器
def logging(flag):
    # 核心不变的点是：定义内部函数，格式要和原函数保持一致  参数和返回值
    def my_sum_sub(fn_name):
        def fn_inner(a, b):
            if flag == "+":
                print("正在努力计算加法中")
            elif flag == "-":
                print("正在努力计算减法中")
            return fn_name(a,b)
        return fn_inner
    return my_sum_sub

# 原函数
# @logging('+')
def get_sum(a, b):
    return a + b

# @logging('-')
def get_sub(a, b):
    return a - b

if __name__ == '__main__':

    # print(get_sum(10, 10))
    # print(get_sub(20, 10))

    # l1 = logging("+")
    # get_sum = l1(get_sum)
    # print(get_sum(20, 10))

    print(logging("+")(get_sum)(10, 20))
