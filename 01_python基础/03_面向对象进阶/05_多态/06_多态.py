"""
    多态：同一个函数，接受不同的参数，有不同的状态

    大白话：
        同一个事务在不同的时刻中表现出不同的状态

    python中多态：前提条件
        1.要有继承
        2.要有方法重写
        3.父类引用指向子类对象

"""
class HeroFighter:
    def power(self):
        return 60


class EnemyFighter:
    def power(self):
        return 70

class TwoHeroFighter(HeroFighter):
    def power(self):
        return 80

# 注意缩进    构建对战平台，公共的函数，接受不同的参数
def object_play(hero, emeny):
    if hero.power() >= emeny.power():
        print("英雄机赢了")
    else:
        print("英雄机惜败")

h1 = HeroFighter()
e1 = EnemyFighter()

object_play(h1,e1)

print(type(object_play))

