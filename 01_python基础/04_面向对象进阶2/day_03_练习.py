# 1：编写一个闭包函数 `outer`，它接受一个参数 `x`，并返回一个内部函数 `inner`。
#       `inner` 函数接受一个参数 `y`，并返回 `x + y` 的结果。测试这个闭包。
print("第一题：")
def outer(x):
    def inner(y):
        return x+y
    return inner



print(outer(5)(5))


# 2：编写一个闭包函数 `counter`，它返回一个内部函数 `increment`。
#   每次调用 `increment` 时，它会增加并返回一个计数器。使用 `nonlocal` 关键字来实现。
print("第二题：")
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count

    return increment

increment = counter()
print(increment())
print(increment())
print(increment())


# 3：编写一个装饰器 `@uppercase`，它将函数的返回值转换为大写。
#       参考函数：upper()_转换为大写
print("第三题：")
def uppercase(fn_name):
    def change(str1):
        return str1.upper()
    return change

@uppercase
def str_r(s):
    return s


print(str_r("sssss"))




#4：编写一个装饰器 `@repeat(n)`，它可以让被装饰的函数重复执行 `n` 次。
print("第四题：")
def repeat(n):
    def zhixing(fn_name):
        def fn_inner():
            for i in range(n):
                fn_name()
        return fn_inner
    return zhixing

def cishu():
    print("执行")

r1 = repeat(3)
r1 = r1(cishu)
r1()

# 5：编写两个装饰器 `@uppercase` 和 `@exclaim`，
#       分别将函数的返回值转换为大写和添加感叹号。测试它们的组合效果。
print("第五题：")
def uppercase(fn_name):
    def fn_inner():
        return fn_name().upper()
    return fn_inner

def exclaim(fn_name):
    def fn_inner():
        return fn_name()+"!"
    return fn_inner

@exclaim
@uppercase
def str_s():
    return "sssss"

print(str_s())

