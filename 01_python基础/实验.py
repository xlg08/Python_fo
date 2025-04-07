class MyYe:
    age = 20
    def __init__(self):
        self.age = 10
        print("初始化MyYe")
class School(MyYe):

    name = "黑马"
    def __init__(self):
        print("初始化School")
        self.name = '黑马程序员'

    def make_cook(self):
        print(f'{self.name}煎饼果子配方')


class Master():
    def __init__(self):
        print("初始化Master")
        self.kongfu = '老师傅'

    def make_cake(self):
        print(f'{self.kongfu}煎饼果子配方')


class Son(Master, School):
    # def make(self):
    pass
        # School.make_cook(self)

# 子类对象在创建时，只会初始化最近的父类，不会初始化远的父类，以及父类的父类
b = Son()
print(b.age)
# print(b.__dir__())
# print(b.name)
# b.make_cook()
# b.name = "55"
# b.make_cook()