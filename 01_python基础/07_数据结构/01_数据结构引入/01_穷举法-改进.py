import time

startTime = time.time()

for a in range(0, 1000):        # a
    for b in range(0, 1000):
        for c in range(0, 1000):        # c
            # 把if里面的加法运算，放到平方运算前面，因为加法运算比平方运算要简洁
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)

endtime = time.time()

print(f"程序的执行时间：{endtime - startTime}")