import socket
server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 8888))
server_socket.listen(5)
accept_socket, client_info = server_socket.accept()
accept_socket.send(b"welcome to you")
data = accept_socket.recv(1024).decode("utf-8")
print(data)
accept_socket.close()