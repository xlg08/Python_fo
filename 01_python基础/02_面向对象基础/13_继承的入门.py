"""

    在python中，所有类默认继承object类，object类是顶级类或基类(超类)；其他子类叫做派生类(衍生类)


    在python中继承格式：
            class 父类名称(object):
                pass
            class 子类名称(父类名称):
                pass
        提示：object是所有类的父类 object类是顶级类或者基类 ，其他的子类派生类
    例如：Father类有一个默认性别为男，且爱好散步行走，那么，Son类也想要拥有这些属性和行为，该怎么办


    继承
        好处：提高了代码复用性
        弊端：耦合性，父类又不好的内容，子类想没有都不行，   高内聚低耦合  （大白话：自己能搞定的事情，不要麻烦别人）

"""

class Father(object):
    def __init__(self):
        self.gender = "男"

    def walk(self):
        print("饭后走一走，活到九十九")
class Son(Father):
    pass

# 测试子类
s1 = Son()
print(s1.gender)
s1.walk()





