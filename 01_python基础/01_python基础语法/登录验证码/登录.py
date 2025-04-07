
# 只给3次机会, 登陆失败要提示剩余次数。
# print()
for i in range(3):      # 0 1 2
    user = input("账号:")
    password = input("密码:")
    if user == 'admin' and password == 'admin888':
        print("登录成功")
        break
    if 2-i == 0:
        print("错误三次,账号锁定")
        break
    print(f"账号或密码错误,请重新输入,剩余{2-i}次")