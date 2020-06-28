import socket

BUF_SIZE = 1024
PORT = 2500

addr = ('localhost', PORT)
sock = socket.create_connection(addr)

while True:
    msg = input("Message to send: ")

    try:
        # sendall()은 전송된 바이트 수를 리턴하지 않음
        sock.sendall(msg.encode())
    except:
        sock.close()
        break

    try:
        rx_data = sock.recv(BUF_SIZE)
    except:
        sock.close()
        break
    else:
        if not rx_data:
            break
        print("Rx msg:", rx_data.decode())
