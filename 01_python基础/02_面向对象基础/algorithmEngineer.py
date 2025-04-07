"""
    定义一个算法工程师类，同时使用`__init__()`初始化岗位名称、薪资金额等属性，
        工作内容是每天码代码，同时使用`__str__()`展示对象所拥有的所有信息。

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