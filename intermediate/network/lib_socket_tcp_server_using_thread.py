from socket import *
import _thread

rx_buf = 1024
host_addr = "127.0.0.1"
port = 2500

def response(key):
    return "Response Msg"

def handler(client_sock, addr):
    while True:
        data = client_sock.recv(rx_buf)
        print("Rx data: " + repr(data))

        if not data:
            break

        client_sock.send(response('').encode())
        print("Tx: " + repr(response('')))

if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((host_addr, port))
    sock.listen(5)

    while True:
        print("Waiting ...")
        client_sock, addr = sock.accept()
        print("Connected: ", addr)
        _thread.start_new_thread(handler, (client_sock, addr))
