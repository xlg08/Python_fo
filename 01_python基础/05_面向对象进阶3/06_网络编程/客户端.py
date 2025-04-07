import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1",8888))
data = client_socket.recv(1024).decode("utf-8")
print(data)
client_socket.send("你好！".encode("utf-8"))
client_socket.close()