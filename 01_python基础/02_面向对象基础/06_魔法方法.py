"""

    魔法方法：
        在python中，有一些可以给python类增加魔力的特殊方法，总是被双下划线所包围，称之为魔法方法
        在特殊情况下会被自动调用，不需要手动调用
        __魔法方法名__()

    内置函数：不管你用不用他都有，就像人生下来就有手有脚
    魔法方法：
        python内置函数，在满足特定的场景下，会被自动调用
    场景魔法方法：
        __init__()      在(每次)创建对象的时候，会自动触发该类__init()函数
        __str__()
        __del__()


"""



class Car:

    # 函数、方法、行为
    def __init__(self):
        print("无参  __init__ 魔法方法")
        self.color = "黑色"
        self.number = 3

# 每次创建一次对象，调用一次init方法
# 创建汽车类对象
c1 = Car()      # 会自动调用init方法
# c1.__init__()   # 手动调用魔法方法
print("*"*30)

c2 = Car()
print(c2.color, c2.number)

c1.color = '蓝色'
c1.number = 4







