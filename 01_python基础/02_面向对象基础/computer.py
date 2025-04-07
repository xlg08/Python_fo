"""
    定义一个电脑类，并给电脑添加品牌、价格等属性，同时电脑能用于编程、看视频。

"""
class Computer:
    def __init__(self):
        self.brand = "联想"
        self.price = 10000

    def programming(self):
        print("正在编程编程。。")

    def movie(self):
        print("正在看视频。。")

