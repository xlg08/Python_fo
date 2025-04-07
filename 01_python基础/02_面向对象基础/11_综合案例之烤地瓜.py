"""

    类：地瓜类
    属性：烤的时间、烤的状态、调料
    行为：烤、添加调料


"""

# SweetPotato   地瓜
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
