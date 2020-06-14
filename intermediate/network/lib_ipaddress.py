import ipaddress
import binascii

# IPv4Address Object
ipv4_str = ipaddress.ip_address('192.0.2.1')
ipv4_int = ipaddress.ip_address(3221225985)
print("IPv4, str: {}, int: {}".format(ipv4_int, ipv4_str))

# IPv6Address Object
ipv6_str = ipaddress.ip_address('2001:DB::1')
ipv6_int = ipaddress.ip_address(42540766411282592856903984951653826561)
print("IPv6, str: {}, int: {}\n".format(ipv6_int, ipv6_str))

print(ipaddress.ip_address(1))	# IPv4Address('0.0.0.1')
print(ipaddress.IPv4Address(1))	# IPv4Address('0.0.0.1')
print(ipaddress.IPv6Address(1))	# IPv6Address('::1')
print()

print("IPv4, str:", str(ipaddress.IPv4Address('172.0.0.1')))
print("IPv4, int:", int(ipaddress.IPv4Address('172.0.0.1')))
print("IPv6, str:", str(ipaddress.IPv6Address('::1')))
print("IPv6, int:", int(ipaddress.IPv6Address('::1')))

a = b'abc'
print("\nhex:{}\n".format(binascii.hexlify(a)))

Addresses = [
    '192.168.0.5',
    '2001:0:9d38:6abd:480:f1f:3f57:fffb',
]

for ipaddr in Addresses:
    addr = ipaddress.ip_address(ipaddr)
    print(f'IP address: {addr!r}')
    print("loopback:", addr.is_loopback)
    print('IP version:', addr.version)
    print('Packed addr:', binascii.hexlify(addr.packed))
    print('Integer address:', int(addr))
    print('Is private?:', addr.is_private)
    print()

