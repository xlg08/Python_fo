"""
    不定长参数，也叫可变参数，用于不确定调用时会传递多少个参数场景(或者一个不传递)

    1.不定长位置参数 (不定长元组参数，可以使用一个元组来接受所有的参数)
        *args  *args参数整体   args变量名  *只是一个符号，没有别的意思
    2.不定长关键字参数 (不定长字典参数)，使用一个字典接受所有的参数
        **kargs  **kwargs 是一个整体    kwargs是一个变量名

    规则：
        1.两者可以单独使用
        2.也可以配合使用，但是*args要放在**kwargs前面。否则报错

"""


# 定义一个不定长位置参数
def fun(*args):
    for i in args:
        print(i)


def fun2(*_):
    for i in _:
        print(i, end="\t")


# fun2("张三", 18, ["name", 18, "hha"])

def func(**kwargs):
    for key in kwargs:
        print(f"{key}:{kwargs[key]}")


func(name="刘备", age=18)

'''

'''


def funcf(*args, **kwargs):
    print()






