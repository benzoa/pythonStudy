from socket import *
import struct

group_addr = ("224.0.0.255", 5005)
sock = socket(AF_INET, SOCK_DGRAM)
sock.settimeout(0.5)

TTL = struct.pack('@i', 2)
sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, TTL)

while True:
    rmsg = input("Message: ")
    sock.sendto(rmsg.encode(), group_addr)

    while True:
        try:
            response, addr = sock.recvfrom(1024)
        except timeout:
            break
        else:
            print('{} from {}'.format(response.decode(), addr))
