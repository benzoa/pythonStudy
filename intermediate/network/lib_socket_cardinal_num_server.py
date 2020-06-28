import socket

table = {'1':'one', '2':'two', '3':'three', '4':'four', \
    '5':'five', '6':'six', '7':'seven', '8':'eight', \
    '9':'nine', '10':'ten'}

sock = socket.socket()  # AF_INET, SOCK_STREAM
sock.bind(("", 2500))
sock.listen(1)

client, client_addr = sock.accept()
print("Connected:", client_addr)

while True:
    data = client.recv(1024).decode()
    try:
        resp = table[data]
    except:
        client.send('Try Again'.encode())
    else:
        client.send(resp.encode())
