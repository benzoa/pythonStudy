import socket
import capsulate

SIZE = 5
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('localhost', 2500))

HEAD = 0x05
addr = 1
seqNo = 1
frame_seq = ""
msg = "Hello World"
print("Tx msg:", msg)

for i in range(0, len(msg), SIZE):
    frame_seq += capsulate.frame(HEAD, addr, seqNo, msg[i:i+SIZE])
    seqNo += 1

sock.send(frame_seq.encode())

msg = sock.recv(2048).decode()
print("Rx msg:", msg)
r_frame = msg.split(chr(0x05))
del r_frame[0]

p_msg = ''
for fr in r_frame:
    p_msg += fr[10:(11+int(fr[6:10]))]

print("reassembled: ", p_msg)
sock.close()
