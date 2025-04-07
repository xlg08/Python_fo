"""
    第一题：
    定义两个变量, title='大白菜'，price=3.5，
        按照如下格式进行输出：今天蔬菜特价了，大白菜只要3.5元/斤。
"""
print("第一题：")
title = '大白菜'
price = 3.5

print("今天蔬菜特价了，%s只要%.1f元/斤。" % (title, price))
print("今天蔬菜特价了，{}只要{}元/斤。".format(title, price))
print(f"今天蔬菜特价了，{title}只要{price}元/斤。")

"""
    第二题：
    定义两个变量, name='孙悟空'，mobile='18878569090'，
        按照以下格式进行输出"姓名：孙悟空，联系方式：18878569090"
"""
print("第二题：")
name = "孙悟空"
mobile = '18878569090'
print("姓名：%s，联系方式：%s" % (name, mobile))
print("姓名：{}，联系方式：{}".format(name, mobile))
print(f"姓名：{name}，联系方式：{mobile}")

"""
    第三题：AA制餐厅
    需求: 假设你是一位很棒的AA制餐厅的服务员，你的任务是计算每位顾客的应付金额。
        输入顾客人数，并赋值给total_friends变量。
        输入总账单数值，并赋值配给 total_bill 变量。
        在账单费用上加上20%的税，并计算最终账单总额均摊给顾客金额，然后打印
"""
print("第三题：")
total_friends = int(input("请输入顾客人数：\n"))
total_bill = eval(input("请输入总账单数值：\n"))
money = total_bill*(1+0.2)/total_friends
print("均摊到顾客的金额为：%.2f元" % ( money ))

"""
    进阶题：
        键盘输入身高，体重，求BMI = 体重(kg)/身高(m)的平方
"""
print("进阶题：")
high = eval(input("请输入您的身高（米）：\n"))
weight = eval(input("请输入您的体重（kg）：\n"))

BMI = weight / (high ** 2)
print("您的BMI为{:.2f}：".format(BMI))
