import re
import socket

LISTEN_ADDR = '127.0.0.1'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((LISTEN_ADDR, PORT))
s.listen(0)

print(('Listening on http://{}:{}/'.format(LISTEN_ADDR, PORT)))

while True:
    conn, addr = s.accept()
    print('Client connected: ' + addr[0])

    while True:
        data = conn.recv(1024)

        if not data:
            break

        if re.search(b'\r*\n\r*\n', data):
            print('Request finished, sending response')
            conn.sendall(b'HTTP/1.1 200 OK\n')
            conn.sendall(b'Content-Type: text/html; charset=utf-8\n\n')
            conn.sendall(b'<h1>Hello, World!</h1>')
            conn.close()
            break
