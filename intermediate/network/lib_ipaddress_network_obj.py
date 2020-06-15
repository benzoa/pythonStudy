import binascii
import ipaddress

ipv4 = ipaddress.ip_network('192.0.2.0/24')
ipv6 = ipaddress.ip_network('2001:db8::0/96')
print("{}, {}".format(ipv4, ipv6))


print("v4, netmask: {}, hostmask: {}".format(ipv4.with_netmask, ipv4.with_hostmask))
print("v6, netmask: {}, hostmask: {}\n".format(ipv6.with_netmask, ipv6.with_hostmask))

ipv4 = ipaddress.ip_network('192.0.2.1/24', strict=False)
print("netmask: {}, hostmask: {}\n".format(ipv4.with_netmask, ipv4.with_hostmask))

print("v4, num_addr: {}".format(ipv4.num_addresses))
print("v6, num_addr: {}\n".format(ipv6.num_addresses))

for x in ipv4.hosts():
    print(x)

print()

print("v4, netmask: {}, hostmask: {}".format(ipv4.netmask, ipv4.hostmask))
print("v6, netmask: {}, hostmask: {}".format(ipv6.netmask, ipv6.hostmask))

print("v6, compressed: {}, exploded: {}".format(ipv6.compressed, ipv6.exploded))

print("ipv4[1]: {}, ipv4[-1]: {}".format(ipv4[1], ipv4[-1]))
print("ipv6[1]: {}, ipv6[-1]: {}".format(ipv6[1], ipv6[-1]))


addr = ipaddress.ip_address('192.0.2.1')
print("%s belong to %s, %s" %(str(addr), str(ipv4), 
    "True" if addr in ipv4 else "False"))


print("compare %s with %s, %s" %(str(addr), str(ipv4), 
    "True" if addr < ipaddress.ip_address('192.0.2.2') else "False"))


print("[0]: {}, [1]: {}".format(ipv4[0], ipv4[1]))


print("hosts: {}".format(list(ipv4.hosts())))
print()

NetAddrs = ['10.9.0.0/24', 'fdfd:87b5:b475:5e3e::/64']

for addr in NetAddrs:
    net = ipaddress.ip_network(addr)
    print(f'Network address: {net!r}')
    print(f'Is private: {net.is_private}')
    print(f'Broadcast address: {net.broadcast_address}')
    print(f'Compressed address: {net.compressed}')
    print(f'Addr with netmask: {net.with_netmask}')
    print(f'Addr with hostmask: {net.with_hostmask}')
    print(f'Num addresses: {net.num_addresses}')
    print()


NETWORKS = [
    '10.9.0.0/24',
    'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    
    for i, ip in zip(range(3), net.hosts()):
        print(ip)
    print()


NETWORKS = [
    ipaddress.ip_network('10.9.0.0/24'),
    ipaddress.ip_network('fdfd:87b5:b475:5e3e::/64'),
]

ADDRESSES = [
    ipaddress.ip_address('10.9.0.6'),
    ipaddress.ip_address('10.7.0.31'),
    ipaddress.ip_address('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa'),
    ipaddress.ip_address('fe80::3840:c439:b25e:63b0'),
]

for ip in ADDRESSES:
    for net in NETWORKS:
        if ip in net:
            print('{}\nis on {}'.format(ip, net))
            break
        else:
            print('{}\nis not on {}'.format(ip, net))
    print()
