import selectors
import socket

def accept_handler(server_sock, sel):
    client_sock, addr = server_sock.accept()
    print(f'Accepted {client_sock.getpeername()} from {addr}')

    # Register client socket
    client_sock.setblocking(False)
    sel.register(client_sock, selectors.EVENT_READ, read_handler)


def read_handler(conn, sel):
  data = conn.recv(1024)
  
  if data:
    print(f'echoing {repr(data)} to 'f'{conn.getpeername()}')
    conn.sendall(data)
  else:
    # Unregister client socket
    print('closing...')
    sel.unregister(conn)
    conn.close()


def run_server(host="127.0.0.1", port=55000):
    sel = selectors.DefaultSelector()

    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(100)
    sock.setblocking(False)	# nonblocking as timeout=0

    # fileObj, events, data=None
    sel.register(sock, selectors.EVENT_READ, accept_handler)

    while True:
        events = sel.select()
        for (key, mask) in events:	# key: SelectorKey instance
            callback = key.data		# key.data: accept_handler(events[0].data)
            callback(key.fileobj, sel)	# key.fileobj: registed socket


if __name__ == '__main__':
    run_server()
