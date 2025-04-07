
def func(name, age, address):
    return ("你的名字是：",name,"你的名字是：",age,"你的地址是",address)

# 调用参数 传参之[位置参数]  正确位置
print(func("张三",20,"北京"))

# 调用参数 传参之 [位置参数]  错误参数
print(func(20,"张三","北京"))

# 形式参数可以和实际参数同名，因为形参是局部的，只有在函数运行时有效，运行后消失

# 调用参数 传参之 [关键字参数]  正确  key:value 打破位置参数，位置依赖
print(func(age=20,address="北京",name="张三"))

def func2(name, age, address,gender="女"):
    return ("你的名字是：",name,"你的名字是：",age,"你的地址是",address)
# 调用参数之缺省的-默认值
print(func2('张三',20,"北京"))


# 注意事项
    # 1.有位置参数时，位置参数必须在关键字参数的前面
# print(func(gender="女","zhangsan",20,"北京"))
# 报错 ：违反了以上约定

