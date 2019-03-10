from twisted.internet import protocol, reactor
from twisted.protocols import basic

class MirrorProtocol(basic.LineReceiver):
    "Handles one request to mirror some text."
    
    def lineReceived(self, line):
        """The client has sent in a line of text. Write out the
        mirrored version."""    
        self.transport.write(line[::-1]+ '\r\n')

class MirrorFactory(protocol.ServerFactory):
    protocol = MirrorProtocol    

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print 'Usage: %s [hostname] [port number]' % sys.argv[0]
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    reactor.listenTCP(port, MirrorFactory(), interface=hostname)
    reactor.run()
