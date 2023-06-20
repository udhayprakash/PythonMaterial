"""
Purpose: To create a dynamic website
"""
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server


def query_param_app(environ, start_response):
    query_string = environ.get("QUERY_STRING", "")
    query_params = parse_qs(query_string)

    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)

    response = []
    for key, value in query_params.items():
        response.append(f"{key}: {value}\n".encode("utf-8"))

    return response


httpd = make_server("localhost", 8000, query_param_app)
httpd.serve_forever()
