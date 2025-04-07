"""
    语法格式：
        1.父类名.父类函数名(self)   精准访问，想找哪个父类，就调用哪个父类
        2.super().父类函数名()       只能访问最近的那个父类，有就用，没有就继续往后找，找不到就报错

"""

class Master(object):
    def __init__(self):
        print("打印1")
        # self.name = "李四"
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print("打印2")
        # self.name = "李四"
        print(f'运用{self.kongfu}制作煎饼果子')
class School(object):
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Prentice(School, Master):
    # 创新
    def __init__(self):
        self.kongfu = "[独创煎饼果子技术]"
        self.lala = [1, 2, 3]

    def make_cake(self):
        self.name = "张三"
        print(f'运用{self.kongfu}制作煎饼果子')

    # 需求：同时满足 独创 & 古法
    def make_master_cake(self):
        print(type(self))   # self的type一直都是 Prentice 的对象
        print(id(self))     # self的内存地址id一直都是不变的，不会产生新的对象
        print(id(self.kongfu))  # self中的与父类重名的属性的内存地址id改变了
        print(self.kongfu)
        # 这里需要初始化父类的self，不然还会调用子类的self 打印独创
        # 此处会用父类的初始化方法中的属性来修改子类中的属性(父类和子类重名的属性)
        Master.__init__(self)
        print(type(self))
        print(id(self))
        print(id(self.kongfu))
        print(self.kongfu)
        Master.make_cake(self)

p1 = Prentice()
p1.make_cake()
p1.make_master_cake()
print(p1.name)