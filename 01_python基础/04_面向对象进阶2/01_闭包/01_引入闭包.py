"""
    引出闭包

"""

# 定义一个函数用于保存变量10，然后调用函数返回值变量并重复累加数值，观察效果

def func():
    number = 10
    return number

num = func()
print(num + 1)      #11   想要的结果是  11
print(num + 1)      #11   想要的结果是  12
print(num + 1)      #11   想要的结果是  13

# 以上无法实现累加，从而引出闭包