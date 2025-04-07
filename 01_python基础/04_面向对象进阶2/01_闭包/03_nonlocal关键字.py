"""
    nonlocal ：
        是一个python内置的关键字，可以实现在内部函数中，修改外部函数的变量值

"""
def fn_outer():
    a = 100
    def fn_inner():
        # 未加nonlocal纸钱 在外部函数的变量的生命周期不同
        # nonlocal关键字用来延长外部函数的变量的生命周期
        # 声明能够让内部函数去修改外部函数的变量
        nonlocal a
        a += 1
        print("a:", a)
    return fn_inner

if __name__ == '__main__':
    a = fn_outer()
    a()
    a()
    a()





