"""
    例如，小明同学当前体重是100kg。
    每当他跑步一次时，则会减少0.5kg；每当他大吃大喝一次时，则会增加2kg。
    请试着采用面向对象方式完成案例。

    类：   学生类
    对象： 小明
    属性： 体重
    行为： 跑步、大吃大喝


"""

class Student:   # 大驼峰
    # 类 = 属性 + 方法（行为）
    def __init__(self):
        self.current_weigth = 100

    # 3.行为：跑步、大吃大喝
    def run(self):
        print("疯狂跑步。。。。")
        self.current_weigth -= 0.5

    def eat(self):
        print("大吃一顿")
        self.current_weigth += 2

    def __str__(self):
        return f"当前体重{self.current_weigth}"


# 4.实例化学生对象
xm = Student()
xm.run()
xm.eat()
print(xm)
