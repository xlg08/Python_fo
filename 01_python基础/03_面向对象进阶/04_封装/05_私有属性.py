"""
    封装：
        属于面向对象的三大特征之一，就是隐藏对象的属性和方法细节，进对外提供公共访问方式
    封装格式：
        属性：__属性
        方法: __方法名()
    封装的原因：
        1.提高代码的安全性  私有化来保障
        2.提高代码复用性    由函数来保障
    弊端：
        代码量增加（公共访问接口），因为私有内容外界想访问，必须提供公共的接口。代码量增加

"""
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'Master：运用{self.kongfu}制作煎饼果子')
class School(object):
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    def make_cake(self):
        print(f'School：运用{self.kongfu}制作煎饼果子')


class Prentice(School, Master):
    # 创新
    def __init__(self):
        self.kongfu = "[独创煎饼果子技术]"
        self.__money = 20000    # 有钱

    def make_cake(self):
        print(f'学徒：运用{self.kongfu}制作煎饼果子')

    def get_money(self):
        return self.__money

    def __set_money(self, money):
        self.__money = money

    # 修改的接口
    def set_money(self, money):
        self.__money = money


class TuSun(Prentice):
    pass

ts = TuSun()
print(ts.kongfu)
ts.make_cake()
# ts.money = 0
# print(ts.money)     # 此处已经将师傅的钱私有化了，即tusun拿不到money这个属性了
# print(ts.getMoney())        # 师傅对外提供的访问接口。只能通过这个接口来访问

# print(ts._Prentice__money)   # python中是伪私有的，他只是改了个名字 _类名__属性或者__方法名
# print(ts.__dir__())         # 查看该对象的所有属性和方法，包括继承下来的父类中私有的

