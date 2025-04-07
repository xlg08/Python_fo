"""
    抽象类就好比定义一个标准，包含了一些抽象的方法，要求子类必须实现

    抽象类（接口）  一般充当父类，是一种标准（行业标准）

        抽象类：包含由抽象方法的类称之为抽象类
        抽象方法：方法体是空实现的（pass）
"""

# 抽象类
class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def wind_l_r(self):
        pass

class Haier(AC):

    def cool_wind(self):
        print("吹冷风")

    def hot_wind(self):
        print("吹热风")

    def wind_l_r(self):
        print("左右摆头")


