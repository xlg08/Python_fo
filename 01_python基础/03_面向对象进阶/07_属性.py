"""
    类或对象中的属性都属于属性

    属性：
        概述：
            用来描述事物特征
        分类：
            对象属性：属于每个对象，即：每个对象的属性值可能不同
            类属性：属于类的，即：能被该类下所有的对象所共享
        对象属性：
            定义到 init魔法方法 的属性。每个对象都有自己的内容
            只能通过 对象名. 的方式调用
        类属性：
            定义到类中，函数外的属性（变量），能被该类下所有的对象所共享
            既能通过 类名. 还能通过 对象名. 的方式来调用，推荐 类名.  方式

    对象属性：
        对象名.属性名
        self.属性名

    类属性：指的就是类所拥有的属性，它被共享于整个类中(即都可以直接调用)。
        类名.类属性名    # 推荐使用
        对象名.类属性名

"""

class Student:
    # 类属性  ：  类中函数外
    teacher_name = "张老师"

    # 定义对象属性  即：定义到 init魔术方法 的属性
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"姓名：{self.name}"

s1 = Student("孔老师")
print(s1)

s2 = Student("王老师")
print(s2)


# 类属性 类名.属性
print(Student.teacher_name)
# 共享
print(s1.teacher_name)
print(s2.teacher_name)

# 更改类属性
Student.teacher_name = "胡老师"
print(Student.teacher_name)
print(s1.teacher_name)
print(s2.teacher_name)

# 改变某一个对象的类属性，只改变该对象的
s1.teacher_name = "王老师"
print(Student.teacher_name)     # 胡老师
print(s1.teacher_name)      # 王老师
print(s2.teacher_name)      # 胡老师

