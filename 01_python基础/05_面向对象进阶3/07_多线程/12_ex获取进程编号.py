"""
    进程编号解释：
        概述：
            在设备中，每个程序（进程）都有用自己的唯一的进程id，当程序释放的时候，该进程id也会释放，
                即：进程id可以重复使用
        目的：
            1.查看子进程得父进程，方便管理
            2.例如：杀死指定进程
        格式;
            方式一：os.getpid() 的使用
            方式二：import multiprocessing
                    pid = multiprocessing.current_process().pid
        细节：main中创建进程，如果没有特殊指定，他的父进程都是main进程
            而main进程的父进程，pycharm程序是pid

"""

# 导入进程工具包
import multiprocessing
import os
import time

# 编写代码
def coding(name, age):
    for i in range(1, 20):
        print(name, age, end='')
        time.sleep(0.01)
        print(f"正在敲第{i}遍代码")
    print(f"p1进程得pid{os.getpid()}, {multiprocessing.current_process().pid},父进程id(ppid):{os.getppid()}")

# 听音乐
def music(name, age):
    for i in range(1, 20):
        print(name,age,end='')
        time.sleep(0.01)
        print(f"正在敲第{i}遍音乐")
    print(f"p2进程得pid{os.getpid()}, {multiprocessing.current_process().pid},父进程id(ppid):{os.getppid()}")


if __name__ == '__main__':

    # 创建两个子进程，并且给进程传递参数
    p1 = multiprocessing.Process(target=coding, args=('小明', 30),name="Processing-1")
    p2 = multiprocessing.Process(target=music, kwargs={'name': '某只🐏', 'age': 33}, name="Processing-1")

    p1.start()
    p2.start()

    print(f"主进程得pid{os.getpid()}, {multiprocessing.current_process().pid},父进程id(ppid):{os.getppid()}")



