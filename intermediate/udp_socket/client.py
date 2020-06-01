import socket

def run_client(host="127.0.0.1", port=55001):
    # IPv4, UDP Socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        while True:
            msg = input(">> ")
            sock.sendto(msg.encode(), (host, port))

            if msg == "bye":
                break

            data, addr = sock.recvfrom(1024)
            print("Received:", data.decode(), "from ", addr[0], ":", addr[1])


if __name__ == "__main__":
    run_client()
