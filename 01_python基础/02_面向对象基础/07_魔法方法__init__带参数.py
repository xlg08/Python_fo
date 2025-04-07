"""
    __init__()魔法方法，在创建对象的时候，会被自动调用。一般用于给该类的属性做初始化


    函数
        def 函数名():  无参函数
        def 函数名(a,b):  有参函数

        有参数的初始化方法 __init__


"""

# 1.创建汽车类，并且初始化带参的方法
class Car:
    # 初始化带参数
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def show(self):
        print(f"颜色{self.color},轮胎数:{self.number}")

c1 = Car()
#2.实例化Car类对象
# c1 = Car("黄色", 4)   # __init__() missing 2 required positional arguments: 'color' and 'number'
# 当带参数初始化方法出现的时候，即在创建对象的时候，可以给对象给予初始化值，否则执行报错
c1.show()