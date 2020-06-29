import lib_socket_server_module as server
import sys

port = 2500

if len(sys.argv > 1):
    port = int(eval(sys.argv[1]))

server_sock = server.TCPServer(port)
client_sock, client_addr = server_sock.accept()

while True:
    print('Connected:', client_sock, client_addr)
    rx_data = client_sock.recv(1024)
    if not rx_data:
        break
    print('rx_data:', rx_data)
    client_sock.send(rx_data)

client_sock.close()
