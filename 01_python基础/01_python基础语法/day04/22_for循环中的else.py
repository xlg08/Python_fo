"""
    循环可以和else配合使用，else下方缩进的代码指的是当循环正常结束之后要执行的代码。
    强调：”正常结束“， 非正常结束，其else中的代码是不会执行的。


    循环无论是while还是for都存在一个特殊结构else
    格式：
        while基本语法：
            while 循环条件：
                ......
            else:
                ......
        小结：
            当循环正常结束后，执行else里面的内容

        for基本语法：
            for 临时变量 in 数据容器:    # for 临时变量 in 序列：
                循环体
                ...
            else:
                当for循环正常结束后，返回的代码
                ...
        小结：当循环正常结束后，执行else里面的内容

    所谓else指的是：循环正常结束后，要执行的代码，即如果出现break情况，则else里面的代码不执行。
    即：循环没有正常结束，则else不执行

"""
def login():
    for a in range(0, 3, 1):
        print(a)
        if a <= 2:
            userName = input("请输入用户名:\n")
            if userName == "admin":
                userPassword = input("请输入密码:\n")
                if userPassword == "admin888":
                    print("登陆成功")
                    break
                print(f"用户名或密码错误，登陆失败,您已输入{a+1}次")
                continue
            print(f"用户名错误，登陆失败,您已输入{a+1}次")
            continue
    else:
        print("您输入错误次数过多，请与管理员联系。")

def login2():
    userName = "admin"
    userPwd = "admin888"

    for i in range(3):
        if i < 3:
            uName = input("请输入您的用户名：\n")
            uPwd = input("请输入您的密码：\n")

            if uName == userName and uPwd == userPwd:
                print("登陆成功")
                break
            else:
                print("登陆失败")
                if i < 2:
                    print(f"您还有{2-i}次机会")
                continue
    else:
        print("输出次数过多，您已无机会。")


if __name__ == '__main__':
    login2()

