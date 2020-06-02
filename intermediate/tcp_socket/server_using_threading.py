import socket
from threading import Thread

def threaded(client_sock, addr):
    print("Connected", addr[0], ":", addr[1])

    while True:
        try:
            data = client_sock.recv(1024)

            msg = data.decode()
            print("Received from " + addr[0], addr[1], msg)

            if msg == 'bye':
                print("Disconnected by " + addr[0], addr[1])
                break

            client_sock.send(data)
        except ConnectionResetError as e:
            # When the client is unexpectedly terminated
            print("Unexpectedly disconnected by " + addr[0], addr[1])
            break
    
    client_sock.close()


def run_server(host="127.0.0.1", port=55000):
    # Ipv4, TCP Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((host, port))
        
        print("Server Start")

        while True:
            # Create a thread when clients connect
            server_sock.listen()
            client_sock, addr = server_sock.accept()
            t = Thread(target=threaded, args=(client_sock, addr))
            t.start()


if __name__ == '__main__':
    run_server()

