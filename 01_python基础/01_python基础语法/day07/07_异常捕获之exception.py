"""
    用 Exception 异常类型捕获可能遇到的所有未知异常

"""


try:
    print(name)
    # print(1/0)
    # str1 = eval(input("请输入："))
    # print(open("a.txt", "r"))
except Exception as e:
    print(e)

print("我还正常！")