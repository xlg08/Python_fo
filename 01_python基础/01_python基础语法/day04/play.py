"""
    1.需求: 数字金字塔
        即: 打印一个由数字组成的金字塔，共n层。例如，当n=5时，输出为：
                1
               121
              12321
             1234321
            123454321
"""
print("第一题：")
while True:
    n = int(float(input("请输入您想生成的层数：\n")))
    if n < 0:
        print("您输入的有误，请重新输入！")
        continue
    # n = 3

    for i in range(1, n + 1):
        for a in range(n - i + 1, 1, -1):
            print(" ", end="\t")
        for a in range(1, i + 1):
            print(a, end="\t")
        for a in range(i - 1, 0, -1):
            print(a, end="\t")
        print()
    else:
        break

"""
    2. 将1 ~ 100之间所有的质数按照3个一行的形式打印到控制台上.
        质数解释:
            1.只能被1 或者 自身整除的整数.
            2.最小的质数是2
"""
print("第二题：")
# n = int(input("您想得到多少以内的质数：\n"))
list2 = []
n = 100
for i in range(2, n+1):
    if i == 2:
        list2.append(i)
        continue
    for a in range(2, int(i**0.5)+1):
        if i % a == 0:
            pass
            break
    else:
        list2.append(i)
        # print(i, end='\t')
print(f"1 ~ {n}以内的质数一共有{len(list2)}个")
b = 0
print("分别为：")
for num in list2:
    if b >= 3:
        print()
        b = 0
    print(num, end="\t")
    b += 1
print()

"""
    3.循环嵌套的方式, 打印99乘法表, 结果如下:
        1 * 1 = 1	
        1 * 2 = 2	2 * 2 = 4	
        1 * 3 = 3	2 * 3 = 6	3 * 3 = 9	
        1 * 4 = 4	2 * 4 = 8	3 * 4 = 12	4 * 4 = 16	
        1 * 5 = 5	2 * 5 = 10	3 * 5 = 15	4 * 5 = 20	5 * 5 = 25	
        1 * 6 = 6	2 * 6 = 12	3 * 6 = 18	4 * 6 = 24	5 * 6 = 30	6 * 6 = 36	
        1 * 7 = 7	2 * 7 = 14	3 * 7 = 21	4 * 7 = 28	5 * 7 = 35	6 * 7 = 42	7 * 7 = 49	
        1 * 8 = 8	2 * 8 = 16	3 * 8 = 24	4 * 8 = 32	5 * 8 = 40	6 * 8 = 48	7 * 8 = 56	8 * 8 = 64	
        1 * 9 = 9	2 * 9 = 18	3 * 9 = 27	4 * 9 = 36	5 * 9 = 45	6 * 9 = 54	7 * 9 = 63	8 * 9 = 72	9 * 9 = 81	
"""
print("第三题：")
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} * {i} = {i*j}", end="\t")
    print()

"""
    4. 键盘录入1个字符串并接收(要求同时包含大写字母, 小写字母, 数字), 统计其中 大写字母, 小写字母, 数字各出现了多少次, 并将结果打印到控制台上.
        例如:
            录入 'abc12345ABCDEF'
        结果是:
            大写字母出现的次数为: 6
            小写字母出现的次数为: 3
            数字出现的次数为: 5
"""
print("第四题：")

str = input("请您输入任意一串字符串：\n")
# str = "abc12345ABCDEF"

a_z = "abcdefghijklmnopqrstuvwxyz"
a_z_List = []

A_Z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A_Z_List = []

num = "0123456789"
num_List = []

# 法一
for a in str:
    for b in a_z:
        if a == b:
            a_z_List.append(a)
            break
    for b in A_Z:
        if a == b:
            A_Z_List.append(a)
            break
    for b in num:
        if a == b:
            num_List.append(a)
            break

# 法二
# for i in str:
#     if 'a' <= i <= 'z':
#         a_z_List.append(i)
#         continue
#     elif 'A' <= i <= 'Z':
#         A_Z_List.append(i)
#         continue
#     elif '0' <= i <= '9':
#         num_List.append(i)
#         continue


print(f"大写字母出现的次数为：{len(A_Z_List)}")
print(f"其中出现的大写字母顺序为：", end="\t")
for i in A_Z_List:
    print(i, end="\t")
else:
    print()

print(f"小写字母出现的次数为：{len(a_z_List)}")
print(f"其中出现的小写字母顺序为：", end="\t")
for i in a_z_List:
    print(i, end="\t")
else:
    print()

print(f"数字出现的次数为：{len(num_List)}")
print(f"其中出现的数字顺序为：", end="\t")
for i in num_List:
    print(i, end="\t")
else:
    print()


"""
    5：回文数是指正读和反读都相同的数。
        例如，121 是回文数。编写程序找出1000以内的所有回文数。

    11 ** 2 = 121
"""
print("增强练习第五题：")
# n = int(eval(input("您想要多少之内的回文数：\n")))
n = 1000
i = 0
list5 = []

while i <= n:

    # 解法一
    yuan_num = i        # 原始数据
    rollback_num = 0        # 反转数字

    while yuan_num > 0:
        num = yuan_num % 10       # 得到最低位
        rollback_num = rollback_num * 10 + num    # 将原始数据的最低位放到反转数字的最高位
        yuan_num = yuan_num // 10       # 将原始数据去掉最低位
    if i == rollback_num:   # 判断原始数据与
        # print(f"{i}是回文数")
        list5.append(i)

    # 解法2
    # a = str(i)
    # b = int(a[::-1])
    # if i == b:
    #     list5.append(i)

    i += 1
else:
    print(f"在{n}以内共有{len(list5)}个回文数。")
b = 0
print("分别为：")
for num in list5:
    if b >= 3:
        print()
        b = 0
    print(num, end="\t")
    b += 1




