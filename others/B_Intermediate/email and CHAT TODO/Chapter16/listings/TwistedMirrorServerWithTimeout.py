#!/usr/bin/python
#This example is BAD! Do not use it!
from twisted.internet import protocol, reactor
from twisted.protocols import basic
import time

class MirrorProtocol(basic.LineReceiver):
    "Handles one request to mirror some text."

    def __init__(self):
        """Set the timeout counter to a value that will always let a
        new user's first request succeed immediately."""
        self.lastUsed = 0
        
    def lineReceived(self, line):
        """The client has sent in a line of text. Write out the
        mirrored version, possibly waiting for a timeout to expire
        before we do. Note: this is a very bad implementation because
        we're running this in a Twisted server, but time.sleep() is a
        blocking call."""
        elapsed = time.time() - self.lastUsed
        print elapsed
        if elapsed < (self.factory.PER_USER_TIMEOUT * 1000):
            time.sleep(self.factory.PER_USER_TIMEOUT-elapsed)
        self.transport.write(line[::-1]+ '\r\n')
        self.lastUsed = time.time()

class MirrorFactory(protocol.ServerFactory):
    "A server for the Mirror protocol defined above."
    protocol = MirrorProtocol    
    PER_USER_TIMEOUT = 5


#This example is GOOD! It uses a method that returns a Deferred object
#(reactor.callLater) and registers a callback with that object.
from twisted.internet import protocol, reactor
from twisted.protocols import basic
import time

class MirrorProtocol(basic.LineReceiver):
    "Handles one request to mirror some text."
    
    def __init__(self):
        """Set the timeout counter to a value that will always let a
        new user's first request succeed immediately."""
        self.lastUsed = 0
        
    def lineReceived(self, line):
        """The client has sent in a line of text. Write out the
        mirrored version, possibly waiting for a timeout to expire
        before we do. This is a good implementation because it uses
        a method that returns a Deferred object (reactor.callLater())
        and registers a callback (writeLine) with that object."""

        elapsed = time.time() - self.lastUsed
        if elapsed < self.factory.PER_USER_TIMEOUT:
            reactor.callLater(self.factory.PER_USER_TIMEOUT-elapsed,
                              self.writeLine, line)
        else:
            self.writeLine(line)

    def writeLine(self, line):
        "Writes the given line and sets the user's timeout."
        self.transport.write(line[::-1] + '\r\n')
        self.lastUsed = time.time()

class MirrorFactory(protocol.ServerFactory):
    "A server for the Mirror protocol defined above."
    protocol = MirrorProtocol    
    PER_USER_TIMEOUT = 5

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print 'Usage: %s [hostname] [port number]' % sys.argv[0]
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    reactor.listenTCP(port, MirrorFactory(), interface=hostname)
    reactor.run()
