"""
    细节：
        编码：把我们看得懂得 转成 我们看不懂的
            '字符串'.encode(码表)

        解码：把我们看不懂的 转成 我们看的懂的
            二进制.decode(码表)

        乱码：编解码格式不一致

        二进制数据的特殊写法 ：即 b 字母、数字、特殊符号


"""

s1 = '黑马1234abc'
print(s1.encode())
print(s1.encode("utf-8"))

# 结论：当没有指定码表的时候默认就是 utf-8

s2 = b'\xe9\xbb\x91\xe9\xa9\xac1234abc'
print(s2.decode())  # 默认解码格式 utf-8


sgbk = s1.encode("gbk")
print(sgbk)
print(sgbk.decode("utf-8"))