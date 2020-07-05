import random
from socket import *

port = 2500
BUFFER = 1024
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFFER)
    if random.randint(1, 10) < 4:
        print("Packet from {} lost!".format(addr))
        continue

    print('msg {!r} from {}'.format(data.decode(), addr))

    sock.sendto('ACK'.encode(), addr)
