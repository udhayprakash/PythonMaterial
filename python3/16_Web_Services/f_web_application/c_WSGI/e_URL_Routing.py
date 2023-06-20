from wsgiref.simple_server import make_server


def home_app(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)

    return [b"Welcome to the home page!"]


def about_app(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)

    return [b"This is the about page."]


def not_found_app(environ, start_response):
    status = "404 Not Found"
    headers = [("Content-type", "text/plain")]
    start_response(status, headers)

    return [b"404 Not Found"]


def router(environ, start_response):
    path = environ.get("PATH_INFO", "").lstrip("/")

    if path == "":
        return home_app(environ, start_response)
    elif path == "about":
        return about_app(environ, start_response)
    else:
        return not_found_app(environ, start_response)


httpd = make_server("localhost", 8000, router)
httpd.serve_forever()
