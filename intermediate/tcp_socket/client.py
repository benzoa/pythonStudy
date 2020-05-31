import socket

def run_client(host="127.0.0.1", port=55000):
    # IPv4, TCP Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((host, port))

        while True:
            msg = input(">> ")
            client_sock.sendall(msg.encode())

            if msg == "bye":
                break
            
            data = client_sock.recv(1024)
            print("Received", repr(data.decode()))


if __name__ == '__main__':
    run_client()
