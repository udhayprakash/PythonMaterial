import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class JSONRPCHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        request = json.loads(body)

        if request['method'] == 'add':
            result = request['params'][0] + request['params'][1]
        else:
            result = None

        response = {
            "jsonrpc": "2.0",
            "result": result,
            "id": request['id']
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, JSONRPCHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()