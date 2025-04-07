"""

多进程实现步骤：
    1. 导入进程工具包
        import multiprocessing
    2. 通过进程类 实例化进程 对象
         子进程对象 = multiprocessing.Process()
    3. 启动进程执行任务
         进程对象.start()



    需求：使用多进程来模拟一边编写代码，一边听音乐功能实现。

"""
import multiprocessing
import time


# 编写代码
def coding():
    for i in range(1, 20):
        time.sleep(0.01)
        print(f"正在敲第{i}遍代码")

# 听音乐
def music():
    for i in range(1, 20):
        time.sleep(0.01)
        print(f"正在敲第{i}遍音乐")

if __name__ == '__main__':

    # 单任务
    # music()
    # coding()


    # 通过进程类 实例化进程 对象
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)

    p1.start()
    p2.start()




