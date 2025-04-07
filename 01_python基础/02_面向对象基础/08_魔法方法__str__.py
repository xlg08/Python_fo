"""
    魔法方法：
        python内置函数，在满足特定的场景下，会被自动调用
    场景魔法方法：
        __init__()      在(每次)创建对象的时候，会自动触发该类__init()函数
        __str__()       当print()函数打印对象的时候，会自动调用该类(所在类)的str魔法方法
                        当前方法默认打印的是对象的内存地址值，无意义，一般都会对方法进行重写改写
                        改写为打印各个属性值
        __del__()


    当使用print输出对象时，默认打印对象的内存地址；
        如实现了__str__()方法，print就自动调用该魔法方法。


"""

# 在输出car对象时，把它的颜色color和轮胎数number属性值显示出来。
class Car:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    # 没有str方法时，打印属性值
    # def show(self):
    #     print(f"颜色{self.color}  轮胎数{self.number}")

    def __str__(self):
        return f"str重新改写后的显示格式：颜色{self.color} 轮胎数{self.number}"


#2.实例化对象
c1 = Car("紫色", 4)
c1.show()

# print(c1)   #
# # 此处其实走了__str__方法，但此处还未对该方法进行重写改写，所以打印的是地址值

# 3.改写str魔法方法
print(c1)   # 此处已重写str




