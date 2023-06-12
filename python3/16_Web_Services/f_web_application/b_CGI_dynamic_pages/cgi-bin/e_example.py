"""
Purpose:

"""
from http.server import BaseHTTPRequestHandler


class GetHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        x = self.wfile.write
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # <--- HTML starts here --->
        x(b"<html>")
        # <--- HEAD starts here --->
        x(b"<head>")
        x(b"<title>Title goes here!</title>")
        x(b"</head>")
        # <--- HEAD ends here --->
        # <--- BODY starts here --->
        x(b"<body>")
        x(b"<p>This is a test.</p>")
        x(b"</body>")
        # <--- BODY ends here --->
        x(b"</html>")
        # <--- HTML ends here --->


if __name__ == "__main__":
    from http.server import HTTPServer

    server = HTTPServer(("localhost", 777), GetHandler)
    print("Starting server, use <Ctrl + F2> to stop")
    server.serve_forever()
