import socket

def getRemoteMachineInfo():
    remoteHost = 'www.python.org'
    try:
        print "IP address: %s"%socket.gethostbyname(remoteHost)
    except socket.error, errMsg:
        print "%s: %s"%(remoteHost, errMsg)

if __name__ == '__main__':
    getRemoteMachineInfo()