"""
    使用多进程来模拟小明一边编写num行代码，一边听count首音乐功能实现。

    进程传参的方式有两种：
        1.args方式：接受所有参数，以元组的方式  （位置参数）
        2.kwargs方式：接受所有参数，以字典的方式  （关键字参数）

"""
# 导入进程工具包
import multiprocessing
import time
import psutil

current_process = psutil.Process()
print(current_process.name())

# 编写代码
def coding(name, age):
    for i in range(1, 20):
        print(name, age, end='')
        time.sleep(0.01)
        print(f"正在敲第{i}遍代码")

# 听音乐
def music(name, age):
    for i in range(1, 20):
        print(name,age,end='')
        current_process = psutil.Process()
        print(current_process.name())
        time.sleep(0.01)
        print(f"正在敲第{i}遍音乐")

if __name__ == '__main__':

    # 创建两个子进程，并且给进程传递参数
    p1 = multiprocessing.Process(target=coding, args=('小明', 30),name="Processing-1")
    p2 = multiprocessing.Process(target=music, kwargs={'name': '某只🐏', 'age': 33}, name="Processing-1")

    p1.start()
    p2.start()
    print(p1.name)

