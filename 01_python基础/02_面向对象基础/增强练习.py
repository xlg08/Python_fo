"""
    > 1. 建`Pet`类，属性：`name`（名字）、`age`（年龄，默认为0）。
    > 2. 方法：
    >    - `birthday()`：年龄增加1岁。
    >      - 打印 xxxx过生日啦！年龄变为xxx 岁
    >    - `display_info()`：显示宠物的名字和年龄
    >      - 打印 宠物名字：xxx，年龄：xxx 岁

"""
print("第一题：")


class Pet:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def birthday(self):
        self.age += 1
        print(f"{self.name}过生日啦！年龄变为{self.age}岁")

    def display_info(self):
        print(f"宠物名字：{self.name}，年龄：{self.age}岁")


pet1 = Pet("佩奇")
pet1.birthday()
pet1.display_info()

"""
    > 1. 创建`Student`类，属性：`name`、`grades`（成绩列表）。
    > 2. 实现`__str__`方法：返回学生姓名和平均成绩。
"""
print("第二题:")


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __str__(self):
        sum = 0
        for i in range(len(self.grades)):
            sum += self.grades[i]
        return f"学生姓名为：{self.name}，平均成绩为{sum / len(self.grades)}"


stu1 = Student("张三", [60, 80, 50, 90, 76, 64])
print(stu1)

"""
    > 1. 创建`Thermometer`类，属性：`current_temp`（当前温度，默认0）。
    > 2. 方法：
    >    - `set_temp(temp)`：设置温度。
    >    - `__str__`：返回当前温度信息。
    >    - `__del__`：删除时提示“温度计已销毁”。
"""
print("第三题:")


class Thermometer:  # 温度计

    def __init__(self):
        self.current_temp = 0

    def set_temp(self, temp):
        self.current_temp = temp

    def __str__(self):
        return f"当前温度为：{self.current_temp}"

    def __del__(self):
        print("温度计已销毁")


t1 = Thermometer()
print("初始温度为：", t1.current_temp)
t1.set_temp(16)
print(t1)
del t1

"""
    1. 创建`AIAssistant`类，属性：`name`（名字）、`skills`（技能列表，默认包含"天气查询"）。
    2. 方法：
       - `learn_skill(new_skill)`：学习新技能并添加到列表。
       - `execute_skill(skill_name)`：执行技能，若未学习则提示“暂不支持该功能”。
       - `__str__`：返回助手状态，如「小爱 | 已掌握技能：天气查询、播放音乐」。
    3. 销毁对象时提示“AI助手已离线”。

"""

print("第四题：")
class AIAssistant:
    def __init__(self, name):
        self.name = name
        self.skills = ["天气查询"]

    def learn_skill(self, new_skill):
        self.skills.append(new_skill)

    def execute_skill(self, skill_name):
        if skill_name in self.skills:
            print(f"执行技能：{skill_name}")
        else:
            print("暂不支持该功能：", skill_name)

    def __str__(self):
        str1 = "、".join(self.skills)
        return f"「{self.name} | 已掌握技能：{str1}」"

    def __del__(self):
        print(f"AI助手{self.name}已离线")

ai1 = AIAssistant("小爱")

ai1.learn_skill("打电话")
print(ai1)
ai1.execute_skill("天气查询")
ai1.execute_skill("玩牌")

del ai1

