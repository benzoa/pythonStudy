import socket, threading

class ClientThread(threading.Thread):
    def __init__(self, sock, addr):
        super().__init__()
        self.client_sock = sock
        print("Add socket:", addr)
    
    def run(self):
        print("Connected:", addr)
        rx_msg = ''

        while True:
            data = self.client_sock.recv(1024)
            rx_msg = data.decode()
            if rx_msg == 'quit':
                break
            print("Rx msg: ", rx_msg)
            self.client_sock.send(bytes(rx_msg, 'UTF-8'))
        
        print("Disconnected:", addr)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("", 2500))
print("Server started ...")

while True:
    server.listen(1)
    client, addr = server.accept()
    t = ClientThread(client, addr)
    t.daemon = True
    t.start()
