"""
    property属性介绍：
        概述/目的/作用
            把函数当作变量来使用
        实现方式：
            方式一：装饰器
            方式二：类属性
        实现方式一：
            property的装饰器用法
                @property                   修饰  获取值的函数  get_age
                @获取值的函数名.setter         修饰  设置值的函数   set_age

    类属性方式：
    类属性 = property(获取值的方式，设置值方式)
"""

# 没有property属性
class student:
    # 私有化属性 age
    def __init__(self):
        self.__age = 18

    # 没有property属性的时候：
    # 提供公共的访问接口  (get/set)
    # @property
    def get_age(self):
    # def age(self):
        return self.__age

    # @get_age.setter
    def set_age(self, age):
    # @age.setter
    # def age(self, age):
        self.__age = age

    age = property(get_age, set_age)


if __name__ == '__main__':
    s1 = student()
    # print(s1.get_age())
    # print(s1.get_age)
    print(s1.age)
    s1.age = 20
    print(s1.age)