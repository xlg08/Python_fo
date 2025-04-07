"""
    形式参数可以与实际参数同名，因为形参是局部的，只有在函数运行时有效，运行后消失


"""


def stu(name, age, address):
    return ("你的名字：", name, "你的年龄：", age, "你的地址：", address)


print(stu("张三", 18, "河北"))
print(stu("张三", 18, "河北"))
print(stu(age=18, name="张三", address="河北"))
print(stu(18, "河北", name="张三"))     # 报错TypeError: stu() got multiple values for argument 'name'





