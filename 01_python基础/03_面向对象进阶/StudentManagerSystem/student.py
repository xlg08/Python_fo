"""
    该文件用于记录学生类，学生属性信息有姓名、性别、年龄、联系方式、描述信息等

"""


class Student:
    """
        对象属性： __init__方法中
    """

    def __init__(self, name, gender, age, phone, desc):
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    # 使用魔法方法进行统一格式输出
    def __str__(self):
        return f"姓名：{self.name}, 性别：{self.gender}, 年龄：{self.age}, 手机号：{self.phone}, 描述信息：{self.desc}"

# s1 = Student("张三", "男", 20, "188888888", "好人")
# print(s1)


if __name__ == '__main__':      # 此处变为程序的入口，在该模块下便不会从上至下执行了
    s1 = Student("张三", "男", 20, "188888888", "好人")
    print(s1)


# def Name():
#     print(__name__)
# Name()