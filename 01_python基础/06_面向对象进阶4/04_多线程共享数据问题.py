"""
    定义一个列表类型的全局变量，创建两个子线程分别执行
    向全局变量添加数据的任务和向全局变量读取数据的任务，
    查看线程之间是否共享全局变量数据

"""
import threading
import time

my_list = []

# 写入数据的任务
def write_data():
    for i in range(10):
        my_list.append(i)
        print("写入数据:", i)
    print(f"调用write_data", my_list)


# 读取数据的任务
def read_data():
    time.sleep(1)
    print("调用write_data:", my_list)


if __name__ == '__main__':
    # 3.创建子线程
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)
    # 4、启动线程
    t1.start()
    # 延时一秒
    # time.sleep(1)
    t2.start()


