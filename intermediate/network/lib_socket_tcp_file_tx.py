import socket
import sys

port = 2500
s = socket.socket()
host=''
s.bind((host, port))
print("waiting for connection ...")
s.listen(1)
c_sock, addr = s.accept()

print("Connected:", c_sock)
msg = c_sock.recv(1024)
print(msg.decode())

file_name = input("File name(c:/test/sample.bin): ")
print(f"Sending '{file_name}'")

fn = file_name.split('/')
print(fn)

c_sock.sendall(fn[-1].encode())

with open(file_name, 'rb') as f:
    c_sock.sendfile(f, 0)

print('Sending complete')
c_sock.close()
