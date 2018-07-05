#!/bin/env python

import sys
import SocketServer
import BaseHTTPServer
import SimpleHTTPServer


class ThreadingSimpleServer(SocketServer.ThreadingMixIn,
                            BaseHTTPServer.HTTPServer):
    pass


if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

server = ThreadingSimpleServer(
    ('', port), SimpleHTTPServer.SimpleHTTPRequestHandler)

try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print "Finished"
