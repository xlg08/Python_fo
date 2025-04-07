"""
    循环代码的执行时间


"""
import time

startTime = time.time()
list1 = []
for i in range(1000000):
    list1.append(i)


endTime = time.time()
print(endTime-startTime)



