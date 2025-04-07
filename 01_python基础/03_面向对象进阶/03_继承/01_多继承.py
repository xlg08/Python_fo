"""
    拓展：MRO机制
        在python中MRO机制，可以查看某个对象，在调用函数的是继承顺序；
            即：在调用过程中，先找哪个类，后找哪个类，

    格式：
        MRO(Method Resolution Order)：方法解析顺序
        类名.mro()
        类名.__mro__

"""

# 1. 师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
            print(f'运用{self.kongfu}制作煎饼果子')

# 为了验证多继承，添加School父类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2. 定义徒弟类，继承师父类 和 学校类
class Prentice(School, Master):     # 继承顺序 从左向右，就近原则
    pass

# 3. 用徒弟类创建对象，调用实例属性和方法
xiaoming = Prentice()
print(xiaoming.kongfu)
xiaoming.make_cake()

print(Prentice.mro())
# print(Prentice.__mro__)
# print(object.__mro__)