import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 50000))
print("Now: ", sock.recv(1024).decode())
sock.close()
