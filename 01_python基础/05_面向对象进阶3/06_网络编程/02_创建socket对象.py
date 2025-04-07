"""

    06_网络编程：
        概述：
            网络编程也叫网络同学，socket通信。即通信双方都有自己的socket对象
        大白话：
            你和你遥远的朋友在聊天的时候，看似你们两个在交互，其实通过手机（双方手机）来交互

"""
# 导包
import socket

# 创建对象
# AddressFamily : 地址簇  即IPv4 还是用IPv6  默认AF_INET (IPv4)  AF_INET6 (IPv6)
# socket type : socket 类型  即 TCP 还是UDP  默认SOCK_STREAM (tcp)  sock_dgram (UDP)
# cr_socket = socket.socket()
cr_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # IPv4 和 TCP
print(cr_socket)
