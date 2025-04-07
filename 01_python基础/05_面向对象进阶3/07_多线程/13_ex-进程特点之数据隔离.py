"""
    前置要求： （了解代码看懂现象）
        进程特点：
            1.进程之间的数据是相互隔离的。
                因为子进程相当于父进程的”副本“。会将父进程的main外资源拷贝一份。即：各是各的
            2.默认情况下，主进程会等待子进程执行结束再结束
"""
import multiprocessing
import time

# 需求：在不同进程中修改列表my_list[]并新增元素，试着在各个进程中观察列表的最终结果。

# 1.定义一个公共的数据容器 my_list[]
my_list = []

# 2.定义函数，向容器中添加数据
def writer_data():
    for i in range(1, 6):
        my_list.append(i)
        print(f"添加数据：{i}")

# 定义函数，从容器中读取数据
def read_data():
    time.sleep(30)
    print(f"read_data函数：{my_list}")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=writer_data)
    p2 = multiprocessing.Process(target=read_data)

    p1.start()
    p2.start()
