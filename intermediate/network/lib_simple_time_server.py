import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('', 50000)
sock.bind(addr)
sock.listen(5)

while True:
    client, addr = sock.accept()
    print("Connected:", addr)
    client.send(time.ctime(time.time()).encode())
    client.close()
