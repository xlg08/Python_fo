"""
    语法结构：
        if 条件判断1：
            成立
        elif 条件判断2：
            成立
        elif 条件判断3：
            成立
        elif 条件判断4：
            成立
        else:
            以上都不成立

"""


month = 13
# if month == 12 or 1 or 2:
#     print("冬季")

if month >= 3 and month <= 5:
    print("春季")
elif month >= 6 and month <= 8:
    print("夏季")
elif month >= 9 and month <= 11:
    print("秋季")
# elif month==12 or(month>0 and month<=2):
# elif month == 12 or (month == 1 or month == 2):
# elif month == 12 or month==1 or month==2:
# elif month == 12 or 1 or 2:  # 错误代码 最终结果都是True
    print("冬季")
else:
    print("您输入的月份不在1-12范围内")


'''
    打工年龄判断
    如果 小于18岁   童工       您的年龄是{},您的工资是0倍
    如果 18~30岁   A级打工人   您的年龄是{},您的工资是1.5倍
    如果 30~50岁   B级打工人   您的年龄是{},您的工资是1.2倍
    如果 50~60岁   C级打工人   您的年龄是{},您的工资是0.5倍
    如果以上都不满足，你已经退休了

'''



age = eval(input("您的年龄是：\n" ))
if 0 <= age < 18:
    print(f"您的年龄是{age}, 您的工资是0倍")
elif 18 <= age < 30:
    print(f"您的年龄是{age}, 您的工资是1.5倍")
elif 30 <= age < 50:
    print(f"您的年龄是{age}, 您的工资是1.2倍")
elif 50 <= age < 60:
    print(f"您的年龄是{age}, 您的工资是0.5倍")
else:
    print("您已经退休了！")

'''
    结论：
    if ... elif ... else ... 为分支语句，
    如果前面的判断语句 成功正确执行，则不会再进行后面的判断。
    
'''
num = 1

if num == 1:
    print("1")
elif num == 1:
    print("2")
else:
    print("2")

