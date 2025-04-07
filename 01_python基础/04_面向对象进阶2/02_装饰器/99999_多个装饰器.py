#1.定义装饰器1
def check_user(fn):
    def inner():
        print("输入用户名和密码")
        fn()
        print("1检查登录内部函数地址：", id(inner))
        print("1检查登录内部函数对象：", inner)
    return inner
#2.定义装饰器2
def check_code(fn):
    def inner():
        print("登录验证码")
        fn()
        print("2检查验证码内部函数地址：", id(inner))
        print("2检查验证码内部函数对象：", inner)
    return inner
# 3. 被装饰器的函数
# @check_user
# @check_code
def comment():
    print("发表评论")



print("*"*50)
# 4.调用函数
comment = check_code(comment)
print("原函数地址：", id(comment))        # 与检查验证码内部函数地址一致
print("原函数对象：", comment)            # 传回的是检查验证码内部函数对象
comment = check_user(comment)
print("原函数地址：", id(comment))        # 与检查登录内部函数地址一致
print("原函数对象：", comment)            # 传回的是检查登录内部函数对象
comment()

print("*"*50)
print("1检查登录装饰器函数地址：", id(check_user))
print("2检查验证码装饰器函数地址：", id(check_code))

# print("返回函数地址：", id(a))

print("1检查登录装饰器函数对象：", check_user)
print("2检查验证码装饰器函数对象：", check_code)

# print("返回函数对象：", a)