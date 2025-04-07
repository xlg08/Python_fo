## 简答题
"""
（2）请简要描述下网络编程的三要素，并分别说说其作用。

    (1)IP地址：这是网络环境下每一台计算机的唯一标识，通过IP地址来找到指定的计算机；
    (2)端口：用于标识进程的逻辑地址，通过端口来找到指定的进程；
    (2)端口：用于标识进程的逻辑地址，通过端口来找到指定的进程；

"""
import socket

"""
（3）请说说TCP网络程序开发的步骤流程。

    TCP服务器程序开发流程；
        1. 创建服务端套接字对象
        2. 绑定端口号
        3. 设置监听
        4. 等待接受客户端的连接请求
        5. 发送数据
        6. 接收数据
        7. 关闭套接字

    TCP客户端程序开发流程。
        1. 创建客户端套接字对象
        2. 客户端连接服务器端
        3. 接收数据
        4. 发送数据
        5. 关闭套接字

"""




## 实操题
"""
（1）将字符串“”转换为二进制bytes类型的结果；
    将二进制bytes数据 b"AI python"转换为字符串str类型的结果。
"""
s1='AI人工智能进阶班'
print(s1)
print(s1.encode(encoding='utf-8'))
s2=b'AI python'
print(s2)
print(s2.decode(encoding='utf-8'))


"""
（2）通过TCP客户端发送消息：欢迎来传智教育，真牛!通过TCP服务器端接收消息，并打印出来。
"""
import socket

# 通过TCP服务器端接收消息，并打印出来。
server_socket=socket.socket()
server_socket.bind(('127.0.0.1',8888))
server_socket.listen(128)
con_socket,address=server_socket.accept()
recv=con_socket.recv(1024).decode(encoding='utf-8')
print(recv)
server_socket.close()

import socket
# 通过TCP客户端发送消息：欢迎来传智教育，真牛!
client_socket=socket.socket()
client_socket.connect(('127.0.0.1',8080))
client_socket.send('欢迎来传智教育，真牛!'.encode(encoding='utf-8'))
client_socket.close()