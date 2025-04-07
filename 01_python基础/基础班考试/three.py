for i in range(3):      # 0 1 2
    user = input("请输入您的账号为:\n")
    password = input("请输入您的密码为:\n")
    if user == 'admin' and password == 'admin888':
        print("恭喜您登录成功！")
        break
    if 2 - i == 0:
        print("您已输入错误3次，不可再输入，请与管理员联系！")
        break
    print(f"您的账号或密码错误,请您重新输入,您剩余的次数为{2-i}次")