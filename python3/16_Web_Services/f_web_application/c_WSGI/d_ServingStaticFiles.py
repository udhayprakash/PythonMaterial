from wsgiref.simple_server import make_server


def static_file_app(environ, start_response):
    path = environ.get("PATH_INFO", "").lstrip("/")

    if not path:
        path = "index.html"

    try:
        with open(path, "rb") as file:
            content = file.read()

        status = "200 OK"
        mimetype = "text/html" if path.endswith(".html") else "text/plain"
        headers = [("Content-type", mimetype)]
        start_response(status, headers)

        return [content]

    except FileNotFoundError:
        status = "404 Not Found"
        headers = [("Content-type", "text/plain")]
        start_response(status, headers)

        return [b"404 Not Found"]


httpd = make_server("localhost", 8000, static_file_app)
httpd.serve_forever()
