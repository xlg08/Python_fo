"""

    单继承就是一个子类只能继承自一个父类，不能继承多个类。
        这个子类会有具有父类的属性和方法。


"""

#一个摊煎饼的老师傅，在煎饼果子界摸爬滚打多年，
# 研发了一套精湛的摊煎饼技术，
# 师父要把这套技术传授给他的唯一的最得意的徒弟。


# 老师傅
class Master(object):
    def __init__(self):
        self.kongfu = "[古法配方]"

    def make_cake(self):
        print(f"采用{self.kongfu}摊煎饼果子")

# Apprentice  徒弟
class Apprentice(Master):
    pass

# 测试  实例化徒弟类
app = Apprentice()
app.make_cake()



