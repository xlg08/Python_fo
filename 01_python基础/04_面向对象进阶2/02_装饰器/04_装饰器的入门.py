"""
    例如，发表评论前，都是需要先登录的。
        先定义有发表评论的功能函数，
        然后在不改变原有函数的基础上，需要提示用户要先登录。
"""
"""
    装饰器：
        概念/作用：本质上就是一个闭包函数
        目的：在不改变原来函数的基础上，对其功能做了增强
        前提条件:
            ①有嵌套
            ②有引用
            ③有返回
            ④有额外功能
        用法：
            格式1 ： 传统写法
                装饰后的函数名 = 装饰器名(被装饰的原函数名)
                装饰后的函数名()  ！！！一般修饰前和修饰后的函数名保持一致
            格式1 ： 语法糖  （推荐）
                在要被 装饰的原函数头上，直接@装饰器名，直接调用原函数即可
"""

# 编写装饰器
# 参数名为被装饰的原函数名,但是不知道谁要调用该装饰器，所以随便写有一个形参列表
def check_login(fn_name):
    def fn_inner():     # 有嵌套
        # 增加额外功能
        print("检验登录！")
        # 访问原函数，即外部函数的引用
        fn_name()

    print("内部函数地址：", id(fn_inner))
    print("内部函数对象：", fn_inner)
    # 返回内部函数对象(名)
    return fn_inner

# 传统写法
def comment():
    print("发表评论")

# 语法糖
# @check_login
# def comment():
#     print("发表评论")

if __name__ == '__main__':

    # 传统写法
    #       装饰后的函数名 = 装饰器名(被装饰的原函数名)
    #       装饰后的函数名()
    # ！！！一般修饰前和修饰后的函数名保持一致
    # comment = check_login(comment)      # comment被修饰后功能变强了，有了校验功能
    # comment()

    a = check_login(comment)      # comment被修饰后功能变强了，有了校验功能
    a()
    # 三个的地址都不同
    print("装饰器函数地址：", id(check_login))
    print("原函数地址：", id(comment))
    print("返回函数地址：", id(a))

    print("装饰器函数对象：", check_login)
    print("原函数对象：", comment)
    print("返回函数对象：", a)



    # 语法糖
    # comment()