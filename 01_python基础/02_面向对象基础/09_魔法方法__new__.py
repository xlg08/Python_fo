
class Car:


    def __new__(cls, *args, **kwargs):
        print("现在被创建")
        print(cls)
        print(args)
        print(kwargs)
        # 关键：创建实例并返回
        instance = super().__new__(cls)
        return instance

    # 2.初始化
    def __init__(self, brand):
        self.brand = brand
        print("有参构造器")
        print("已初始化")


    # 3.打印对象属性值
    def __str__(self):
        return f"品牌：{self.brand}"

    # 4.删除对象时给提示
    def __del__(self):
        print(f"{self}对象被删除了")


# 5.创建汽车类对象
c1 = Car("小米")
print(c1)  # 验证：str  #程序执行结束后自动删除

# 6.演示手动删除


print("程序结束")





