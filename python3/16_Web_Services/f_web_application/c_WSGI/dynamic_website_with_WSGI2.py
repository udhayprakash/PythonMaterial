from wsgiref.simple_server import make_server

"""
Purpose: To create a dynamic website

WSGI - Web Server Gateway Interface
     - It is a specification that describes how web servers communicate with web applications.
     - WSGI has been specified in PEP 3333.
"""


def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])

    fh = open("question.txt")
    lines = [fh.readline().encode("utf-8") for i in range(30)]

    return lines


server = make_server("localhost", 8080, application)
server.serve_forever()
