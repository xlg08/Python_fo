"""
    with ... open ... 语法介绍：
        概述；
            可以理解为语法糖
            省略文件资源释放close函数
        即：with的语句执行完毕后，会自动释放资源，无需手动释放
        本质：
            是一个上下文管理器，会自动调用close函数，完成资源释放
        格式：
            with open (路径,"模式","编码") as 变量名 ,open(...) as 变量名
                此处编写正常的代码

"""
import os

# 文件拷贝
with open("1.png","rb") as src_f,open("2.jpg","wb") as tar_f:
    while True:
        data = src_f.read(2048)
        if len(data) == 0:
            break
        # 将读取到的文件写道目标文件中(2.jpg)
        tar_f.write(data)


