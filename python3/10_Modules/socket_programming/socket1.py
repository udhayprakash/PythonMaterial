import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('https://www.w3.org', 80))
mysock.send('GET http://www.w3.org/TR/PNG/iso_8859-1.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if len(data) < 1 :
        break
    print(data)

mysock.close()
