"""
Purpose: To create a dynamic website

WSGI - Web Server Gateway Interface
     - It is a specification that describes how web servers communicate with web applications.
     - WSGI has been specified in PEP 3333.
"""
from wsgiref.simple_server import make_server


def hello_world_app(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, World!"]


httpd = make_server("localhost", 8000, hello_world_app)
httpd.serve_forever()
