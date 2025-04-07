"""
    假如创建一个子线程，这个子线程执行完大概需要2.5秒钟，
    现在让主线程执行1秒钟就退出程序，查看一下执行结果


"""

import threading
import time


def work():
    for i in range(20):
        time.sleep(0.25)
        print(f"{i}次工作")

if __name__ == '__main__':
    # 2.创建子线程

    # 方式一：创建子线程时指定守护线程 daemon=True
    # t1 = threading.Thread(target=work, daemon=True)

    # 方式二
    t1 = threading.Thread(target=work)
    t1.setDaemon(True)
    # t1.daemon = True

    # 3.启动线程
    t1.start()
    time.sleep(1)
    print("主线程执行完毕")
