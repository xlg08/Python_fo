"""
    例如，发表评论前，都是需要 先登录用户 再进行 验证码验证。
    先定义有发表评论的功能函数，然后在不改变原有函数的基础上，需要先检查用户登录和输入验证码

    多个装饰器装饰一个原函数，就按照 由内向外 的顺序来装饰
    但是用 装饰器写法来做，看到是效果是从上往下执行

    语法糖：从上往下
    传统写法：从内往外
"""

# 装饰器 1
def check_login(fn_name):
    def fn_inner():
        print("校验登录")
        fn_name()
    return fn_inner

# 装饰器 2
def check_code(fn_name):
    def fn_inner():
        print("校验验证码")
        fn_name()
    return fn_inner

# 原函数
# @check_login
# @check_code
def comment():
    print("发表评论")

# 测试
# 传统写法
comment = check_code(comment)
comment = check_login(comment)
comment()

# 语法糖
# comment()