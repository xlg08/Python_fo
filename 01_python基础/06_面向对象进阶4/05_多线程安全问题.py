"""
    多线程共享全局变量，出现的问题
        累加次数不够

    产生原因：
        线程1还没有来得及执行完（一个整个的工作），就被线程2抢走了资源，就可能出现问题
    解决方案：
        加锁思想： 互斥锁
    细节：使用互斥锁的时候，要再合适的时候释放锁，可能出现死锁或者锁不住

"""
import threading

# 定义两个函数，实现循环100万次，每循环一次给全局变量加1，
# 创建两个子线程执行对应的两个函数，查看计算后的结果

global_num = 0
def fun1():
    global global_num
    for i in range(100000000):
        global_num += 1
    print(f"fun1的函数结果{global_num}")

def fun2():
    global global_num
    for i in range(100000000):
        global_num += 1
    print(f"fun2的函数结果{global_num}")




if __name__ == '__main__':
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)

    t1.start()
    t2.start()

# 注意！！！ 如果是python3.12 python底层做了一些优化，加了一些锁，第二个打印的值。 200W