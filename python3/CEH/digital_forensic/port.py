import socket

RemoteIP = 'IP Address to be Scanned'
PortList = [20, 22, 23, 80, 135, 445, 912]
for CurrentPort in PortList:
    CurrentSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
resultset = CurrentSocket.connect_ex((RemoteIP, CurrentPort))
print
CurrentPort, ":", resultset
CurrentSocket.close()
