import binascii
import socket
import struct
import sys

print("Ipv4 .........................")
for string_address in ['203.249.39.46','127.0.0.1']:
    packed = socket.inet_aton(string_address)
    print ('Original:', string_address)
    print ('Packed  :', binascii.hexlify(packed))
    print ('Unpacked:', socket.inet_ntoa(packed))
    print ()


print("Ipv6 .........................")
string_address ='2002:ac10:10a:1234:21e:52ff:fe74:40e'

packed =socket.inet_pton(socket.AF_INET6 ,string_address)
print ('Original:',string_address)
print ('Packed  :',binascii.hexlify(packed))
print ('Unpacked:',socket.inet_ntop(socket.AF_INET6 ,packed))
