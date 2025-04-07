"""
    1. 创建客户端套接字对象
    2. 客户端连接服务器端
    3. 接收数据
    4. 发送数据
    5. 关闭套接字


"""

import socket

# 1. 创建客户端套接字对象
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2. 客户端连接服务器端
# client_socket.connect(("192.168.13.62", 8888))
# client_socket.connect(("127.0.0.1", 8888))
# client_socket.connect(("192.168.13.188", 8888))
client_socket.connect(("192.168.13.58", 8888))
# 3. 接收数据
data = client_socket.recv(1024).decode("utf-8")
print(f"客户端收到：{data}")
# 4. 发送数据
client_socket.send("***********-".encode("utf-8"))
# 5. 关闭套接字
client_socket.close()
