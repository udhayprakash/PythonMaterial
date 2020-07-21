#!/bin/env python

import sys
import socketserver
from http.server import HTTPServer
import http.server


class ThreadingSimpleServer(socketserver.ThreadingMixIn,
                            HTTPServer):
    pass


if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

server = ThreadingSimpleServer(
    ('', port), http.server.SimpleHTTPRequestHandler)

try:
    print('Connect at 127.0.0.1:8000')
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print('Finished')
