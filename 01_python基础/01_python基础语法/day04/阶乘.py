"""
    计算阶乘！
    n！ = n * (n-1) * (n-2) * ··· ···
"""

while True:
    n = int(input("请输入一个正整数用以计算阶乘：\n"))
    # n = 3
    if n >= 0:
        amass = 1
        for i in range(n, 1, -1):
            amass = i * amass
        else:
            print(amass)
            break
    else:
        print("您输入有误！请重新输入")



