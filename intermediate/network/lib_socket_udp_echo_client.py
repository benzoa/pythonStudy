import socket

port = 2500
BUFF = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input("Tx msg: ")

sock.sendto(msg.encode(), ('localhost', port))
rx_data, addr = sock.recvfrom(BUFF)
print("Rx Data:", rx_data.decode(), "from", addr)
