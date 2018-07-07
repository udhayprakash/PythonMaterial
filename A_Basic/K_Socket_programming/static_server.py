#!/usr/bin/env python3
import os

from http.server import HTTPServer, BaseHTTPRequestHandler


class StaticServer(BaseHTTPRequestHandler):
    def do_GET(self):
        root = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            ), 'html')
        # print(self.path)
        if self.path == '/':
            filename = root + '/index.html'
        else:
            filename = root + self.path

        self.send_response(200)
        if os.path.splitext(filename)[1] == 'css':
            self.send_header('Content-type', 'text/css')
        elif os.path.splitext(filename)[1]  == 'json':
            self.send_header('Content-type', 'application/javascript')
        elif os.path.splitext(filename)[1]  == 'js':
            self.send_header('Content-type', 'application/javascript')
        elif os.path.splitext(filename)[1]  == 'ico':
            self.send_header('Content-type', 'image/x-icon')
        else:
            self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fh:
            html = fh.read()
            # html = bytes(html, 'utf8')
            self.wfile.write(html)


def run(server_class=HTTPServer, handler_class=StaticServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()


if __name__ == '__main__':
    run()
