'''模拟登陆, 只给3次机会,
登录成功则程序结束,
登陆失败则提示剩余登陆次数.
'''
import random
str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def vscode():
    n = ""
    for i in range(4): n += str1[random.randint(0, len(str1) - 1)]
    return n
def check():
    while True:
        newcode = vscode()
        print('验证码为：', newcode)
        code = input('验证码错误！\n重新输入验证码(区分大小写)：')
        if newcode == code:
            break


for t in range(3):
    m = vscode()
    username = input('请输入用户名：')
    password = input('请输入密码：')
    print('验证码为：', m)
    code = input('输入验证码(区分大小写)：')
    if (username == 'a') and (password == 'a'):
        if m != code:
            check()
            print('登陆成功！')
            break
    else:
        print('用户或密码错误！请重新输入！')
        print(f'您还有{2-t}次机会！')
        if t == 2:
            print('登陆错误！')
