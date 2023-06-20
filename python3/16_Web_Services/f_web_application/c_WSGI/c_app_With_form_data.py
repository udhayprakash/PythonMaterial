"""
Purpose: To create app with form data
"""
from wsgiref.simple_server import make_server


def form_data_app(environ, start_response):
    content_length = int(environ.get("CONTENT_LENGTH", 0))
    form_data = environ["wsgi.input"].read(content_length).decode("utf-8")

    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)

    return [f"Form Data: {form_data}".encode("utf-8")]


httpd = make_server("localhost", 8000, form_data_app)
httpd.serve_forever()
