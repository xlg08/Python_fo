"""
    1. 创建客户端socket对象
    2. 连接服务器端 ip 和 端口
    3. 关联数据源文件 读取内容 ， 写给服务器端
    4. 释放资源

"""

import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.13.62", 9999))
# 3. 关联数据源文件 读取内容 ， 写给服务器端
with open("1.jpg", "rb") as src_f:
    while True:
        data = src_f.read(1024)
        print(data)
        # 发给给服务器
        client_socket.send(data)
        if len(data) == 0:
            break
print("客户端收到消息")
client_socket.close()