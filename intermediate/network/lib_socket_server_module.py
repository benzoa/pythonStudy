class TCPServer:
    def __init__(self, port):
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))
        self.sock.listen(1)
    
    def accept(self):
        self.client_sock, self.client_addr = self.sock.accept()
        return self.client_sock, self.client_addr


if __name__ == '__main__':
    sock = TCPServer(2500)
    client_sock, client_addr = sock.accept()
    print("Connected:", client_sock, client_addr)
    client_sock.send("Hi Client".encode())
    client_sock.close()
