"""
    线程使用步骤:
        1.导包
        2.创建线程对象
        3.启动线程

    线程和进程的关系：
        1.进程是CPU分配资源的基本单位，线程是CPU调度资源得最小单位
        2.线程依附与进程的。每个进程至少有一个线程（主线程）
        3.进程间数据是相互隔离的。（同一个进程）线程间的数据是可以共享的

"""

import time, threading


# 编写代码
def coding():
    for i in range(1, 20):
        time.sleep(1)
        print(f"正在敲第{i}遍代码")


# 听音乐
def music():
    for i in range(1, 20):
        time.sleep(1)
        print(f"正在敲第{i}遍音乐")

if __name__ == '__main__':
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music())


    t1.start()
    t2.start()

    # 在此次可以实现三个线程相互抢资源,因为要让两个子线程也要启动
    for i in range(10):
        time.sleep(1)
        print("主线程")
