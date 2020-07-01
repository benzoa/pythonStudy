import socket

sock = socket.socket()
host = "localhost"
port = 2500

sock.connect((host, port))
sock.send("Ready".encode())
fn = sock.recv(1024).decode()

save_name = 'd:/'
with open(save_name + fn, 'wb') as f:
    print("file opend")
    print('receiving file...')
    while True:
        data = sock.recv(8192)

        if not data:
            break

        f.write(data)

print("Download complete")
sock.close()
