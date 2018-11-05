from wsgiref.simple_server import make_server

"""
Purpose: To create a dynamic website 

WSGI - Web Server Gateway Interface
     - It is a specification that describes how web servers communicate with web applications.
     - WSGI has been specified in PEP 3333. 
"""


def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    # "404 NOT FOUND", "500 SERVER ERROR"
    return ["Hello my friend!".encode("utf-8")]


server = make_server('localhost', 8080, application)
server.serve_forever()
