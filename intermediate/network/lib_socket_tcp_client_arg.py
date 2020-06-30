import socket
import sys
import argparse

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
parser = argparse.ArgumentParser()
parser.add_argument('-s', default="127.0.0.1")
parser.add_argument('-p', type=int, default=2500)
args = parser.parse_args()

sock.connect((args.s, args.p))
print("Connected:", args.s)

while True:
    txData = input("Tx msg: ")
    if len(txData) == 0:
        txData = ''
    if txData == 'q':
        break
    sock.send(txData.encode())
    print("Rx msg: {}\n".format(sock.recv(1024).decode()))

sock.close()
