"""

    重写也叫作覆盖，就是当子类属性或方法与父类的属性或方法名字相同时，从父类继承下来的成员可以重新定义！
	    子类重写父类的属性和方法, 优先会调用子类的属性和方法
    如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法的时候，调用到的是子类里面的同名属性和方法


    子类继承父类，并且在子类中存在和父类  "同名方法"

    重写：
        重写也叫覆写，即子类出现和父类【重名】的属性或者方法。称之为重写
        调用层次：就近原则 子类用子类的，没有就去找父类的，依次按照继承顺序去找其他父类

"""
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
            print(f'运用{self.kongfu}制作煎饼果子')
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Prentice(School, Master):
    # 创新
    def __init__(self):
        self.kongfu = "[独创煎饼果子技术]"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 3. 用徒弟类创建对象，调用实例属性和方法
xiaoming = Prentice()
print(xiaoming.kongfu)
xiaoming.make_cake()