#!/usr/bin/env python3
print("Content-Type: text/html\n")
print("<!doctype html><title>Hello</title><h2>hello world</h2>")


"""
USAGE:

    $ python3 -m http.server --bind localhost --cgi 8000

    $ chmod +x cgi-bin/a_hello.py

    $ python -m webbrowser http://localhost:8000/cgi-bin/a_hello.py

"""
