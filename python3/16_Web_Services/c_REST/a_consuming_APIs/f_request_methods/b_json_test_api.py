#!/usr/bin/python
"""
Purpose: To demonstrate the usage of API

https://jsonplaceholder.typicode.com/

All HTTP methods are supported.

    GET	    /posts
    GET	    /posts/1
    GET	    /posts/1/comments
    GET	    /comments?postId=1
    GET	    /posts?userId=1
    POST	/posts
    PUT	    /posts/1
    PATCH	/posts/1
    DELETE	/posts/1
"""
from pprint import pprint

import requests

URL = "https://jsonplaceholder.typicode.com"  # text/html


def get_response(url):
    response = requests.get(url)
    if response.ok:
        print(
            f'\n{response.headers["Content-Type"]}'
        )  # application/json; charset=utf-8
        if "application/json" in response.headers["Content-Type"]:
            pprint(response.json())
    else:
        print(f"\n{response.status_code =}")
        print(f"{response.url         =}")
        print(f"{response.reason      =}")
        # print(f'{response.ok          =}')
        # print(f'{response.is_redirect =}')
        # print(f'{response.is_permanent_redirect =}')


if __name__ == "__main__":
    get_response(URL + "/posts")
    get_response(URL + "/posts/1")
    get_response(URL + "/posts/comments")
    get_response(URL + "/comments?postId=1")
