# 在有参无返回值的原有函数求和计算结果纸钱，添加一个友好提示（注意：不能改变源码）：正在努力计算中

# 装饰器
def my_sum(fn_name):
    def fn_inner(x, y):     # 有嵌套
        print("正在计算")       # 有增强
        fn_name(x, y)       # 有引用
    return fn_inner     # 有返回

# 【原函数】有参无返回值的原有函数求和
@my_sum
def get_sum(a, b):
    sum = a + b
    print("sum求和结果是：", sum)

if __name__ == '__main__':
    get_sum(10, 20)