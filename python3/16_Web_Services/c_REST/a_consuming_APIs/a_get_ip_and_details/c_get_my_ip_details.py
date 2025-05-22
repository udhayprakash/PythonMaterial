#!/usr/bin/python
"""
Purpose: Getting IP details

    GET https://ipapi.co/{format}/

python -m pip install -U requests --user
"""
from security import safe_requests


def get_response(url):
    file_extension = url.split("/")[-1] or "html"
    response = safe_requests.get(url, timeout=60)
    with open("result.{}".format(file_extension), "wb") as f:
        f.write(response.content)
        f.close()


if __name__ == "__main__":
    get_response("https://ipapi.co/")
    get_response("https://ipapi.co/json")
    get_response("https://ipapi.co/yaml")
    get_response("https://ipapi.co/csv")
