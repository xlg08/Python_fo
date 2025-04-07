"""
（1）请写出单继承与多继承的语法格式?

    单继承：
        # 父类Father
        class Father(object):
            pass
        # 子类Son
        class Son(Father):
        pass

    多继承：
        # 父类1Father
        class Father(object):
            pass
        # 父类2Mother
        class Mother(object):
            pass
        # 子类Son
        class Son(Father,Mother):
            pass
"""

"""
（2）什么是方法重写，为什么要方法重写?
    重写也叫覆写，即子类出现和父类【重名】的属性或者方法。称之为重写
        调用层次：就近原则 子类用子类的，没有就去找父类的，依次按照继承顺序去找其他父类
    使用方法重写的原因是：可以让子类在使用父类的方法时，可以具有自己特色功能
    
"""


#（4）实操练习：
"""
    1.创建一个Animal（动物）基类，其中有一个run方法，输出`跑起来....`；
"""
class Animal:
    def run(self):
        print("跑起来....")

an = Animal()
an.run()

"""
    2.创建一个Horse（马）类继承于动物类，Horse类中不仅有run()方法还有eat()方法；
        2.1run方法输出 `跑起来....`
        2.2 eat 方法输出 `吃东西...`
"""
class Horse(Animal):

    def eat(self):
        print("吃东西...")

ho = Horse()
ho.run()
ho.eat()


"""
    （5）编写一下多态场景
        构建对象对战平台object_play
        1 英雄一代战机（战斗力60）与敌军战机（战斗力70）对抗。英雄1代战机失败！
        2 卧薪尝胆，英雄二代战机（战斗力80）出场！，战胜敌军战机！
        3 对象对战平台object_play, 代码不发生变化的情况下, 完成多次战斗
"""

class OneHeroFighter:
    def power(self):
        return 60


class EnemyFighter:
    def power(self):
        return 70

class TwoHeroFighter(OneHeroFighter):
    def power(self):
        return 80

def object_play(hero, emeny):
    if hero.power() >= emeny.power():
        print("英雄机赢了")
    else:
        print("英雄机惜败")

h1 = OneHeroFighter()
e1 = EnemyFighter()

object_play(h1,e1)

h2 = TwoHeroFighter()
object_play(h2, e1)


"""
    (6) 编写一下抽象类场景
        国家部门制定了打印机标准
        1、请抽象父类，制定标准：
            抽象printer，要求支持黑白打印(Black_white_printing)、彩色打印(color_printing)。
        2、完成打印机hp、小米、佳能（canon）硬件入围；入围测试平台 make_test_printing(myobj:抽象类))
        3、完成多态场景测试
"""
class Printer:
    def black_white_printing(self):
        pass
    def color_printing(self):
        pass

class Hp(Printer):

    def black_white_printing(self):
        print("hp进行黑白打印")

    def color_printing(self):
        print("hp进行彩色打印")

class XiaoMi(Printer):
    def black_white_printing(self):
        print("小米进行黑白打印")

    def color_printing(self):
        print("小米进行彩色打印")

class Canon(Printer):
    def black_white_printing(self):
        print("佳能进行黑白打印")

    def color_printing(self):
        print("佳能进行彩色打印")

def make_test_printing(myobj:Printer):
    myobj.black_white_printing()
    myobj.color_printing()

hp = Hp()
xiaoMi = XiaoMi()
canon = Canon()
make_test_printing(hp)
make_test_printing(xiaoMi)
make_test_printing(canon)
