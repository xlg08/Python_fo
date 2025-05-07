import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.108.88", 8000))
client_socket.send("hello，itheima".encode("utf-8"))
data = client_socket.recv(1024).decode("utf-8")
print(f"接受到服务器的端发送来的消息：{data}")
client_socket.close()