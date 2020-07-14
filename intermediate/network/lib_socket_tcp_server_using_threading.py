import socket
import threading

def handler(client, addr):
    global connections
    while True:
        data = client.recv(1024)

        for conn in connections:
            conn.send(bytes(data))
        
        if not data:
            connections.remove(client)
            client.close()
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 2500))
sock.listen(1)
connections = []

while True:
    client, addr = sock.accept()
    t = threading.Thread(target=handler, args=(client, addr))
    t.daemon = True
    t.start()

    connections.append(client)
    print(connections)
