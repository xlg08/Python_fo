"""

    类方法:
        所谓类方法，指的是类所拥有的方法，并需要使用装饰器@cssmelathod来标识其为类方法，
        同时一定要注意的是对于类方法的第一个参数必须是类对象，通常以cls作为第一个参数名。

        @classmethod
        def 类方法名(cls):
            ...

        类名.类方法名    # 推荐使用
        对象名.类方法名

    静态方法：
        静态方法需要通过装饰器@staticmethod来标识其为静态方法，且静态方法不需要多定义参数。

        @staticmethod
        def 静态方法名():
            ...

        类名.静态方法名    # 推荐使用

        对象名.静态方法名

    类方法：
        属于类的方法，可以通过 类名. 方式进行调用 还可以通过 对象名. 方式
        定义类方法的时候，必须使用装饰器 @classmethod，且第一个参数必须是类对象

    静态方法：
        属于该类的所有对象所共享的方法，可以通过 类名. 方式  还可以通过 对象名. 方式
        定义静态方法的时候，必须使用装饰器 @staticmethod，且参数传不传都可以

    区别：
        1.类方法第一个参数必须是类对象，静态方法对参数无无特殊要求
        2.理解为：如果函数中要用到类对象，就定义为类方法，否则定义为静态方法


"""
class Student:
    # 类属性
    school = "黑马"

    @classmethod
    def show1(cls):
        print("aaa")
        print(cls.school)
        print("类方法")

    @staticmethod
    def show2():
        print(Student.school)
        print("静态方法")

s1 = Student()
s1.show1()

s1.show2()






