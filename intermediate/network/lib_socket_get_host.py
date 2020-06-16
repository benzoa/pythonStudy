import socket

print("hostname: %s\n" %socket.gethostname())

HOSTS = [
    'www.google.co.kr',
    'pymotw.com',
    'www.python.org',
    'testname',
]

for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host, msg))
print()

for host in HOSTS:
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print('- Hostname:', name)
        print('- FQDN:', socket.getfqdn(name))
        print('- Aliases :', aliases)
        print('- Addresses:', addresses)
    except socket.error as msg:
        print('ERROR:', msg)
    print()

hostname, aliases, addresses = socket.gethostbyaddr('66.33.211.242')

print('Hostname :', hostname)
print('Aliases  :', aliases)
print('Addresses:', addresses)
