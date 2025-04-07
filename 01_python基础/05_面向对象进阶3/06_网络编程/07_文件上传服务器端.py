"""
    1.创建socket对象
    2.绑定ip、端口号
    3.设置最大监听数
    4.等待客户端申请连接
    5.读取客户端上传的文件数据，写入到目的文件
    6.释放资源

"""

import socket
# 1.创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.绑定ip、端口号
server_socket.bind(("192.168.13.58", 9999))
# 3.设置最大监听数
server_socket.listen(5)
# 4.等待客户端申请连接
accept_socket, client_info = server_socket.accept()
# 5.读取客户端上传的文件数据，写入到目的文件

file_name = "./data/1"
file_suffix = ".jpg"

with open(file_name + file_suffix, "wb") as dats_f:
    # 5.1 循环读取
    while True:
        # 5.2
        data_bys = accept_socket.recv(1024)
        if len(data_bys) == 0:
            break
        dats_f.write(data_bys)

# 6.释放资源
accept_socket.send(("文件上传成功！").encode("utf-8"))
accept_socket.close()

