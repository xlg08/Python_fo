### 简答题
"""
（2）说一说为什么主进程创建子进程的代码块需要写在“if __name__ == '__main__':下

    ‌必要性：这是Python多进程编程的最佳实践，防止意外的进程递归和模块副作用。
    官方推荐：Python官方文档明确要求将进程启动代码放在if __name__ == '__main__':中，以确保跨平台行为一致。
    扩展性：此约定不仅适用于multiprocessing，也适用于任何需要在模块化环境中控制代码执行流的场景。
"""






### 实操题
"""
（1）请使用多任务形式完成：一边编程、一边听音乐、一边跟同事聊天。要求如下：
    a.使用多进程完成；
    b.执行效果图。
"""
import multiprocessing
import time

def coding():
    for i in range(1, 20):
        time.sleep(1)
        print(f'第{i}次编程')


def music():
    for i in range(1, 20):
        time.sleep(1)
        print(f'第{i}次听音乐')


def chat():
    for i in range(1, 20):
        time.sleep(1)
        print(f'第{i}次聊天')


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)
    p3 = multiprocessing.Process(target=chat)

    p1.start()
    p2.start()
    p3.start()



