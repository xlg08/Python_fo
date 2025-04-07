"""
    进程特点：
        1.进程之间的数据是相互隔离的。
            因为子进程相当于父进程的”副本“。会将父进程的main外资源拷贝一份。即：各是各的
        2.默认情况下，主进程会等待子进程执行结束再结束
            思路1：设置子进程为"守护"进程
            思路2：强制关闭子进程，可能会导致子进程变为僵尸进程。
                交由python解释器自动回收(底层有init初始化进程来进行严格管理)

"""
import multiprocessing
import time


def work():
    for i in range(100):
        print("工作")
        time.sleep(0.2)

if __name__ == '__main__':

    # p1 进程
    p1 = multiprocessing.Process(target=work)

    # 思路一：设置守护进程   为p1设置守护进程    （人在塔在）
    # p1.daemon = True

    p1.start()

    # 主进程（main）休眠1s后结束
    time.sleep(1)

    # 思路二：强制关闭子进程
    p1.terminate()


    print("main进程结束了")