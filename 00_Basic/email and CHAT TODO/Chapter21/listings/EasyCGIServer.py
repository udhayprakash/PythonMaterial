from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
HTTPServer(('localhost', 8000), CGIHTTPRequestHandler).serve_forever()
