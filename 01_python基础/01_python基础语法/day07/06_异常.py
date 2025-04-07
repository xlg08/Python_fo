"""
    异常：
    try:
        可能发生错误的代码
    except
        如果出现异常执行的代码

    异常解决的是程序在运行过程中可能出现的一些错误
    编写时的语法错误，python 解释器的都过不了，更谈不上异常

"""

# 背景：如果几千行、几万行代码因为某一行或者某几行代码直接导致程序报错退出！！
# 不允许出现这样的情况。给与解决方案！！！

# 如果解决 ？   让抓住这个异常，让这个异常不影响我们其他代码功能运行
# 抓这个异常的错误信息，把他保存为文件（线上运行日志）



# 如何处理  ？ 异常格式：
"""
    try:
        可能出现异常的代码
    except:
        捕获后对代码进行处理
    
"""

# try:
#     filename = open("hahha.avi","r")
#     print(filename.read())
#     filename.close()
# except:
#     print("出异常喽！")
# # 没有影响后续
# print('我还能出现哦')

# 获取异常信息
try:
    filename = open("hahha.avi","r")
    print(1 / 0)
except ZeroDivisionError as b:
    print(b)
except FileNotFoundError as a:
    print(a)
    print("捕获到了")

print('我还能出现哦')



