import gc
import random


def captcha(n):
    """
    生成任意位数的验证码验证码
    :param n:   生成的位数
    :return:    验证码
    """
    str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = ""
    for i in range(n):
        a = random.randint(0, len(str1) - 1)
        num += str1[a]
    return num



# print(captcha(10))


# set_1 = {a, b, c, d, e}
# for i in range(10):
#     a, b, c, d = "a", "b", "c", "d"
#     e = a + b
#     set_1 = {a, b, c, d, e}
#     print(f"a:{hash(a)}\tb:{hash(b)}\tc:{hash(c)}\td:{hash(d)}\te:{hash(e)}")
#     # print(f"a:{id(a)}\tb:{id(b)}\tc:{id(c)}\td:{id(d)}\te:{id(e)}")
#     print(set_1)
#     del a
#     del b
#     del c
#     del d
#     del e
#     print(a)
#     # gc.collect()
# print(set_1)

a = "张三"
print(hash(a))
del a
gc.collect()
# print(hash(a))
a = "张三"
print()