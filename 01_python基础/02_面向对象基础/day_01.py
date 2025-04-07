### 简答题
"""
（1）举例说明生活中的案例：分别以面向过程、面向对象方式思考

    面向过程思考方式：
        如将大象装入冰箱:
            1. 确定冰箱门状态和大象
            2.打开冰箱门
            3.放入大象
            4.关闭冰箱门

    面向对象思考方式：
        如一个冰箱：
            属性：长宽高、容积
            方法：制冷

"""

"""
（2）说一说类和对象是什么？

    类：抽象的概念，看不见，摸不着   类=属性（生活：名词   编程：变量） + 方法（生活：动词（行为）  编程：函数）
    对象：类的具体体现   类的实现（实例化一个类）
    
    类是模板：对现实事物的抽象描述
    对象：显示事物的具体体现
    
"""

### 实操题
"""
（1）定义一个手机类，能开机、能关机、可以拍照。
"""
class Phone:
    def open(self):
        print(f"{self}开机了")
    def close(self):
        print(f"{self}关机了")
    def photo(self):
        print(f"{self}拍照")

p1 = Phone()
p1.photo()

"""
（2）定义一个电脑类，并给电脑添加品牌、价格等属性，同时电脑能用于编程、看视频。
"""
class Computer:
    def __init__(self):
        self.brand = "联想"
        self.price = 10000

    def programming(self):
        print("正在编程编程。。")

    def movie(self):
        print("正在看视频。。")

"""
（3）尝试定义一个算法工程师类，同时使用`__init__()`初始化岗位名称、薪资金额等属性，工作内容是每天码代码，
        同时使用`__str__()`展示对象所拥有的所有信息。
"""

class AlgorithmEngineer:

    def __init__(self,post,salary):
        self.post = post
        self.salary = salary

    def programming(self):
        print("正在码代码。。。")

    def __str__(self):
        return f"{self.post}岗位的薪资是：{self.salary}元"

ae = AlgorithmEngineer("算法工程师",10000)
ae.programming()
print(ae)

"""
（4）独立编写一遍课堂案例：减肥案例
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


xm = Student()
xm.run()
xm.eat()
print(xm)

"""
（5）独立编写一遍课堂案例：烤地瓜案例
"""
class SweetPotato:

    # 类 = 属性 + 行为
    def __init__(self):
        self.cook_time = 0
        self.cook_state = "生的"
        self.seasoning = []     # 添加调料

    # 烤
    def cook(self, time):
        if time < 0:
            print("无效值")
        else:
            # 假设time 传递的时间为2 即该语句为 0+2 ， 相当于2分钟，如果再传5分钟 2+5=7  熟了
            self.cook_time += time
            if 0 <= self.cook_time < 3:
                self.cook_state = "生的"
            elif 3 <= self.cook_time < 7:
                self.cook_state = "半生不熟"
            elif 7 <= self.cook_time < 12:
                self.cook_state = "熟了"
            else:
                self.cook_state = "糊了"

    def addSeasoning(self, seasoning):
        # self.seasoning = seasoning
        self.seasoning.append(seasoning)

    def __str__(self):
        return f"烤的时间{self.cook_time}，地瓜状态{self.cook_state}，调料{self.seasoning}"

# 实例化对象
sp= SweetPotato()

# 初始化地瓜的状态
print(sp.cook_time)
print(sp.cook_state)
print(sp.seasoning)

#
sp.cook(2)
print(sp)
sp.cook(5)
print(sp)
sp.addSeasoning("玛莎拉")
sp.addSeasoning("胡椒")
sp.addSeasoning("辣椒")
print(sp)

print("==", SweetPotato.__base__())





















