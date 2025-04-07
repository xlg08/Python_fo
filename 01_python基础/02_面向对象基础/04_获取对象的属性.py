"""
    属性设置：
        【属性赋值】    对象名.属性名 = 属性值
        【属性调用】    对象名.属性名

    类外 设置属性
        对象名.属性名 = 属性值
    特点：该属性独属于这个对象。即该类的其他对象没有这个属性

    类内 设置属性


"""

class Car:

    def run(self):

        print("汽车会跑")


# 类外  创建该类的对象名  ---->    此位置  类外
c1 = Car()
c1.run()

# 细节1：对c1设置属性值
c1.color = "红色"
c1.number = 4

# 细节2：打印c1的对象属性值
print(f"颜色：{c1.color},轮胎数：{c1.number}")

print("*"*24)

# 定义其他对象
c2 = Car()
c2.run()


# 分析：报错，c2尝试去color和number，因为c1设置是类外属性，仅仅对c1有效，c2找不到
print(c2.color)
print(c2.number)
