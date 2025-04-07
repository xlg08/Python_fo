import threading
import time


# 使用多线程来模拟小明一边编写num行代码，一边听count首音乐功能实现。

def coding(name, num):
    for i in range(num):
        time.sleep(0.01)
        print(f"{name}正在敲{i}行代码")

def munsic(name, count):
    for i in range(count):
        time.sleep(0.01)
        print(f"{name}正在听{i}首歌")


# args 元组
# kwargs 字典
t1 = threading.Thread(target=coding, args=("小明", 50))
t2 = threading.Thread(target=munsic, args=("小明", 50))
t1.start()
t2.start()