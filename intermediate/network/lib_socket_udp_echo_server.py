import socket

port = 2500
BUFF = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    rx_data, addr = sock.recvfrom(BUFF)
    print("Rx Data:", rx_data.decode(), "from", addr)
    sock.sendto(rx_data, addr)
