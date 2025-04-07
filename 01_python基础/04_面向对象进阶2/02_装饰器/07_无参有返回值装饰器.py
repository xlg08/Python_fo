# 装饰器
def my_sum(fn_name):
    def fn_inner():     # 有嵌套
        print("正在努力计算中。。。")       # 有增强
        return fn_name()       # 有引用
    return fn_inner     # 有返回

# 【原函数】有参无返回值的原有函数求和
@my_sum
def get_sum():
    a = 10
    b = 20
    sum = a + b
    return sum

if __name__ == '__main__':
    print("计算结果是：", get_sum())