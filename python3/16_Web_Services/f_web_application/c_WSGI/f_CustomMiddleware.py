from wsgiref.simple_server import make_server


def middleware_app(app):
    def middleware(environ, start_response):
        # Do something before calling the actual app
        # ...

        response = app(environ, start_response)

        # Do something with the response
        # ...

        return response

    return middleware


def hello_world_app(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, World!"]


app = middleware_app(hello_world_app)

httpd = make_server("localhost", 8000, app)
httpd.serve_forever()
