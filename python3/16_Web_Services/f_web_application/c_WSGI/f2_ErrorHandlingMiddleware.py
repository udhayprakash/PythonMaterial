from wsgiref.simple_server import make_server


def error_handling_middleware(app):
    def middleware(environ, start_response):
        try:
            response = app(environ, start_response)
        except Exception as e:
            status = "500 Internal Server Error"
            headers = [("Content-type", "text/plain")]
            start_response(status, headers, sys.exc_info())

            response = [str(e).encode("utf-8")]

        return response

    return middleware


def hello_world_app(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, World!"]


app = error_handling_middleware(hello_world_app)

httpd = make_server("localhost", 8000, app)
httpd.serve_forever()
