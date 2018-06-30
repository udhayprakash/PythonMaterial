from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler).serve_forever()
