"""

    object 与 type 的关系
        object 是类型系统的基类，而 type 是元类（用于创建类的类）。

看似矛盾的现象：
    print(isinstance(object, type))     # True（object 是 type 的实例）
    print(isinstance(type, object))     # True（type 是 object 的子类）
    这是 Python 类型系统的一个特殊设计，  object 和 type 互相依赖，形成闭环。

"""

"""
    object 没有父类的原因：
        object 是类型系统的终极起点，
            用于保证所有类共享统一的基础行为（如 __str__、__repr__ 等方法）。
        如果 object 有父类，Python 的类型系统将陷入无限递归逻辑。

"""


class Father(object):
    def __init__(self):
        self.gender = "男"

    def walk(self):
        print("饭后走一走，活到九十九")

class NewBase(object):
    pass

class Son(Father):
    pass

class Sun(Son):
    pass

# 测试子类
# s1 = Son()
# print(s1.gender)
# s1.walk()
#
# print(Son.__bases__)
# Son.__bases__ = (NewBase,)      # 直接修改Son的基类，改变Son的继承关系
# print(Son.__bases__)

s2 = Sun()
print(Sun.__bases__)
print(isinstance(s2, Father))       # True 属于Father一脉
Sun.__bases__ = (NewBase,)      # 直接修改Son的基类，改变Son的继承关系
print(Sun.__bases__)
print(isinstance(s2, Father))       # False 不再是Father的孙

print(Sun.mro())

# Sun.__mro__ = (None,object,)     # 在python中继承树属性用户不可写，用户无权限写


# python ： builtins(内置)模块


