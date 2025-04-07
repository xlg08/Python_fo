"""
    1.类的定义  class 类名
    2.类中方法 类中函数
        三个函数

    类定义格式
        class 类名：
            属性 （变量）
            方法 （函数）         行为=方法=函数

    访问  ： 类中行为访问
        类内：self.
        类外：对象名.




"""


class Phone:
    def open(self):
        print(f"{self}开机了")
    def close(self):
        print(f"{self}关机了")
    def photo(self):
        print(f"{self}拍照")

# 创建手机类对象 = 实例化手机类对象  访问其成员 (方法、属性)
# 都是一个对象
p1 = Phone()
p1.photo()