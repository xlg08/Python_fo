import threading

global_num = 0

# 在全局位置创建锁
# 创建一个锁
lk = threading.Lock()

# def fun1():
#     lk.acquire()
#     global global_num
#     for i in range(100000000):
#         global_num += 1
#     print(f"fun1的函数结果{global_num}")
#     lk.release()


# def fun2():
#     lk.acquire()
#     global global_num
#     for i in range(100000000):
#         global_num += 1
#     print(f"fun2的函数结果{global_num}")
#     lk.release()

def fun1():
    global global_num
    lk.acquire()
    for i in range(1000000):
        global_num += 1
    lk.release()
    print(f"fun1的函数结果{global_num}")


def fun2():
    global global_num
    lk.acquire()
    for i in range(1000000):
        global_num += 1
    lk.release()
    print(f"fun2的函数结果{global_num}")


# def fun1():
#     global global_num
#     for i in range(1000000):
#         lk.acquire()
#         global_num += 1
#         lk.release()
#     print(f"fun1的函数结果{global_num}")
# def fun2():
#     global global_num
#     for i in range(1000000):
#         lk.acquire()
#         global_num += 1
#         lk.release()
#     print(f"fun2的函数结果{global_num}")



if __name__ == '__main__':
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)

    t1.start()
    t2.start()

# 注意！！！ 如果是python3.12 python底层做了一些优化，加了一些锁，第二个打印的值。 200W