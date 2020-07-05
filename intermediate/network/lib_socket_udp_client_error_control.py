import random
from socket import *

port = 2500
BUFFER = 1024
server = "localhost"

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect((server, port))

for i in range(10):
    delay = 0.1
    data = 'Hello message'

    while True:
        sock.send(data.encode())
        print("Waiting up to {} secondes for a reply".format(delay))
        sock.settimeout(delay)

        try:
            data = sock.recv(BUFFER)
        except timeout:
            delay *= 2
            if delay > 2.0:
                print("The server seems to be down")
                break
        else:
            print('Response:', data.decode())
            break
