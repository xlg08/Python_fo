# 斐波那契数列
"""
    斐波那契数列是 F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) 的数列，形成 0,1,1,2,3,5,8...

"""

n = int(input("请输入您想输入的斐波那契数列的项数：\n"))

list = []
# n = 5

a, b = 0, 1
if n >= 2:
    list.append(a)
    list.append(b)
elif n >= 1:
    list.append(a)
else:
    print("您输入的项数有误！")

# 等价于
# (list.append(a), list.append(b)) if n >= 2 else list.append(a) if n >= 1 else print("您输入的项数有误！")
if n >= 3:
    for i in range(2, n):

        c = a
        a = b
        b = c + b

        # 等价于
        # a, b = b, a + b

        list.append(b)
if n > 0:
    print(list)




