import time

startTime = time.time()

for a in range(0, 1000):        # a
    for b in range(0, 1000):
        for c in range(0, 1000):        # c
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print(a, b, c)

endtime = time.time()

print(f"程序的执行时间：{endtime - startTime}")