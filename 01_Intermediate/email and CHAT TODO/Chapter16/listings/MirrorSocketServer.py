#!/usr/bin/python
import SocketServer

class RequestHandler(SocketServer.StreamRequestHandler):
    "Handles one request to mirror some text."

    def handle(self):
        """Read from StreamRequestHandler's provided rfile member,
        which contains the input from the client. Mirror the text
        and write it to the wfile member, which contains the output
        to be sent to the client."""        
        l = True
        while l:
            l = self.rfile.readline().strip()
            if l:
                self.wfile.write(l[::-1] + '\r\n')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print 'Usage: %s [hostname] [port number]' % sys.argv[0]
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])

    SocketServer.TCPServer((hostname, port), RequestHandler).serve_forever()
