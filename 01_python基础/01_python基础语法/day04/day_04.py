# import random
# """
#     1.键盘录入3个整数并接收, 将其最大值打印到控制台上.
#         思路1: if语句.
# """
# import random
#
# list1 = []
# for i in range(3):
#     a = int(input("请您输入一个整数：\n"))
#     list1.append(a)
# print(list1)
# if list1[0] > list1[1] and list1[0] > list1[2]:
#     print(f"你输入的数值中最大值为：{list1[0]}")
# elif list1[1] > list1[2]:
#     print(f"你输入的数值中最大值为：{list1[1]}")
# else:
#     print(f"你输入的数值中最大值为：{list1[2]}")
#
# # 等价于
# # max_value = max(list1[0], list1[1], list1[2])
# # print(max_value)
#
# """
#     2.循环实现计算 1 ~ 100之间的奇数和, 并将结果打印到控制台上.
#         思路1: while循环.
#         思路2: for循环.
# """
# num = 0
# for i in range(1, 100, 2):
#     num += i
# print(f"1 ~ 100之间的奇数和：{num}")
#
#
# """
#     3. 猜数字游戏, 随机生成1个 1 ~ 100之间的数字, 让用户来猜, 并进行对应的提示.
# """
#
# a = random.randint(1, 101)
# # print(a)
# while 1:
#     b = eval(input("您觉得这个数字是多少："))
#     if a > b:
#         print("猜的有点小呦！")
#     elif a < b:
#         print("猜的有点大呦！")
#     else:
#         print("恭喜您猜对了！")
#         break
#
# """
#     4. 模拟登陆, 只给3次机会, 登录成功则程序结束, 登陆失败则提示剩余登陆次数.
# """
# userName = 'admin'
# userPwd = 'admin888'
# for i in range(3):
#     uName = input("请输入您的用户名：\n")
#     uPwd = input("请输入您的密码：\n")
#     if uName != userName or uPwd != uPwd:
#         if i < 2:
#             print(f"登陆失败！您还可以登录{2-i}次")
#     else:
#         print("恭喜您登陆成功！")
#         break
# else:
#     print("对不起，您输入错误次数过多，已超出机会！")
#
#
#
# """
#     5. 打印水仙花数, 将所有的水仙花数 及 水仙花数的总个数 打印到控制台上.
#         水仙花数解释:
#             1.水仙花数是1个三位数.
#             2.它的各个位数的立方和相加等于它本身.
#         例如:
#             153 = 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3  它就是1个水仙花数.
#         提示:
#             水仙花数一共有4个
# """
#
# sum = 0
# list1 = []
#
# for i in range(100,1000):
#     if (i//100) ** 3 + ((i % 100)//10) ** 3 + (i % 10) ** 3 == i:
#         sum += 1
#         # print(i)
#         list1.append(i)
# else:
#     print(f"100~999之间的水仙花数一共有{sum}个，为{list1}")

# 解法二：
# for A in range(1, 10, 1):
#     for B in range(0, 10, 1):
#         for C in range(0, 10, 1):
#             if A ** 3 + B ** 3 + C ** 3 == A * 100 + B * 10 + C:
#                 print(A * 100 + B * 10 + C)

# 解法三：
# for num in range(100, 1000, 1):
#     str_num = str(num)
#     bw = int(str_num[0])
#     sw = int(str_num[1])
#     gw = int(str_num[2])
#     if bw ** 3 + sw ** 3 + gw ** 3 == num:
#         print(num)