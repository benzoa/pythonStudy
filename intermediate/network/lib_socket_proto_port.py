import socket
from urllib.parse import urlparse

URLS = [
    'http://www.python.org',    # http: 80
    'https://www.mybank.com',   # https: 443
    'ftp://prep.ai.mit.edu',    # ftp : 21
    'gopher://gopher.micro.umn.edu',    # gopher : 70
    'smtp://mail.example.com',  # smtp : 25
    'imap://mail.example.com',  # imap : 143
    'imaps://mail.example.com', # imaps : 993
    'pop3://pop.example.com',   # pop3 : 110
    'pop3s://pop.example.com',  # pop3s : 995
]

for url in URLS:
    parsed_url = urlparse(url)
    print(parsed_url)

    port = socket.getservbyname(parsed_url.scheme)
    print('{:>6} : {}\n'.format(parsed_url.scheme, port))

for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
    url = '{}://example.com/'.format(socket.getservbyport(port))
    print(url)
print()

def get_constants(prefix):
    return {
        getattr(socket, n):n
        for n in dir(socket)
        if n.startswith(prefix)
    }

protocols = get_constants('IPPROTO_')
print("protocols: %s\n" %protocols)

for name in ['icmp','udp','tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print('{:>4} -> {:2d} (socket.{:<12} = {:2d})'.format(
        name, proto_num, const_name, getattr(socket ,const_name)))
