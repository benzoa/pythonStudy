from socket import *

ECHO_PORT = 2500
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', ECHO_PORT))
sock.listen(1)
client, (remotehost, remoteport) = sock.accept()
print("Connected:", remotehost, remoteport)

while True:
    try:
        rx_data = client.recv(BUF_SIZE)
    except:
        client.close()
        break
    else:
        if not rx_data:
            break

        print("Rx message:", rx_data.decode())
    
    try:
        client.send(rx_data)
    except:
        client.close()
        break
