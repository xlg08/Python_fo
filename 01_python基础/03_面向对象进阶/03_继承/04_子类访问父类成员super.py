class Master(object):
    def __init__(self):
        print("打印1")
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print("打印2")
        print(f'Master：运用{self.kongfu}制作煎饼果子')
class School(object):
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    def make_cake(self):
        print(f'School：运用{self.kongfu}制作煎饼果子')


class Prentice(School, Master):
    # 创新
    def __init__(self):
        self.kongfu = "[独创煎饼果子技术]"

    def make_cake(self):
        print(f'学徒：运用{self.kongfu}制作煎饼果子')

    # 需求：同时满足 独创 & 古法
    def make_old_cake(self):
        # 根据就近原则，先找最近的爹School，如果最近的爹没有则找下一个爹，最后一个爹是object
        super().__init__()
        # Master().__init__()
        super().make_cake()
        # Master().make_cake()

p1 = Prentice()
print(p1.kongfu)
p1.make_cake()
print("*"*24)
p1.make_old_cake()