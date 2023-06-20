import json
from http.server import BaseHTTPRequestHandler

data = {"message": "Hello, World!"}


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        data = json.loads(post_data)

        # Perform create operation using the data

        self.send_response(201)
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


if __name__ == "__main__":
    from http.server import HTTPServer

    server = HTTPServer(("localhost", 8000), MyHandler)
    print("Server running on localhost:8000...")
    server.serve_forever()
