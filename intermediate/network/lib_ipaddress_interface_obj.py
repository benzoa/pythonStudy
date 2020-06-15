import ipaddress
import socket

ipv4 = ipaddress.ip_interface('192.0.2.1/24')
ipv6 = ipaddress.ip_interface('2001:db8::1/96')
print("{}, {}".format(ipv4, ipv6))

ADDRESSES = [
    '10.9.0.6/24',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64',
]

print("My Domain: ", socket.getfqdn())
print("My Ip: %s\n" %socket.gethostbyname(socket.getfqdn()))
ADDRESSES.append(socket.gethostbyname(socket.getfqdn()) + '/24')

for ip in ADDRESSES:
    iface = ipaddress.ip_interface(ip)
    print('{!r}'.format(iface))
    print('ip:', iface.ip)
    print('network:', iface.network)
    print('IP with prefixlen:', iface.with_prefixlen)
    print('netmask:', iface.with_netmask)
    print('hostmask:', iface.with_hostmask)
    print()
