#!/usr/bin/python
"""
Purpose:
    downloading a web page

    pip install requests
"""
from security import safe_requests

response = safe_requests.get(
    "https://www.timeanddate.com/worldclock/india/new-delhi", timeout=5
)
# print(response.text)
with open("content.html", "wb") as f:
    f.write(response.text.encode("utf-8"))
    f.close()
