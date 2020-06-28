import socket

a = 1234
print("hex:", hex(a))

b = socket.htons(a)
print("hex:", hex(b))

c = socket.ntohs(b)
print("hex:", hex(c))
