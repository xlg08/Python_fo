"""

    案例：网络编程的入门
        服务器给客户端发送消息，客户端给服务器回执信息

    1. 创建服务端套接字对象
    2. 绑定端口号
    3. 设置监听
    4. 等待接受客户端的连接请求
    5. 发送数据
    6. 接收数据
    7. 关闭套接字


    细节：客户端和服务器都是流程  字节流的形式实现的

"""

# 0.导包
import socket

# 1. 创建服务端套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定端口号
server_socket.bind(("localhost", 8888))
# 3. 设置监听
server_socket.listen(5)
while True:
    try:
        # 4. 等待接受客户端的连接请求   (拆包)
        accept_socket, client_info = server_socket.accept()
        # 5. 发送数据
        # b 是指把数据转换成二进制 (字母、数字、特殊符号)
        accept_socket.send(b"welcome to socket")
        # 6. 接收数据
        data = accept_socket.recv(10024).decode("utf-8")
        print(f"服务器端收到来自{client_info}的信息：{data}")
        # 7. 关闭套接字
        accept_socket.close()   # 关闭监听
        # server_socket.close()   # 关闭服务器端套接字 服务器端一般不关闭
    except:
        pass