import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('', 50000)
sock.bind(addr)
sock.listen(5)
client_sock, addr = sock.accept()
client_sock.send("message".encode())

while True:
    client, addr = socket.accept()
    print("Connected:", addr)
    client.send(time.ctime(time.time()).encode())
    client.close()
