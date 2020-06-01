import socket

def run_server(host="127.0.0.1", port=55001):
    # IPv4, UDP Socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((host, port))
        print("Start Server")

        while True:
                msg, addr = sock.recvfrom(1024)
                print("Received:", msg.decode(), "from", addr[0], ":", addr[1])

                if msg == 'bye':
                    print("Disconnected by " + addr[0], addr[1])
                    break

                # echo
                sock.sendto(msg, addr)


if __name__ == "__main__":
    run_server()

