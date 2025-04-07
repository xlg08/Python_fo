#   编写一个函数 `greet`，接受一个参数 `name`，并返回字符串 `"Hello, [name]!"`。
print("第一题：")


def greet(name):
    return f"Hello,[{name}]!"


print(greet("小马"))

# 编写一个函数 `add`，接受两个参数 `a` 和 `b`，返回它们的和。
#   如果 `a` 或 `b` 不是数字，返回 `"参数必须是数字"`。
print("第二题：")


def add(a, b):
    if a.isdigit() and b.isdigit():
        return eval(a) + eval(b)
    else:
        return '参数必须是数字'


a = input("请输入数字：")
b = input("请输入数字：")
print(add(a, b))
# 编写一个函数 `average`，接受任意数量的参数，返回这些参数的平均值。
print("第三题：")

def average(*args):
    sum = 0
    # print(len(args))
    for i in args:
        sum += i
    return sum / len(args)


print(average(10, 20, 30, 40, 50, 60))

# 编写一个函数 `outer`，在函数内部定义另一个函数 `inner`，
#   `inner` 函数返回传入参数的平方。
#   `outer` 函数返回 `inner` 函数的调用结果。
print("第四题：")
x = eval(input("请您输入一个数用于计算平方数：\n"))


def inner(a):
    return a ** 2


def outer(a):
    return inner(a)


print(outer(x))

# 编写一个函数 `modify_global`，在函数内部修改全局变量 `x = 10`，将其值改为 `20`。
#   使用 `global` 关键字。
print("增强练习第五题：")
x = 10
print(f"x修改前为{x}")


def modify_global():
    global x
    x = 20


modify_global()
print(f"x修改后为{x}")

# 使用 `lambda` 表达式编写一个函数，接受两个参数 `x` 和 `y`，返回它们的乘积。
print("第六题：")
a = lambda x, y: x * y
print(a(4, 5))

# 编写一个列表推导式，生成一个包含1到20之间所有偶数的平方的列表。
print("第七题：")
list7 = []
[list7.append(i ** 2) for i in range(2, 21, 2)]
print(list7)
