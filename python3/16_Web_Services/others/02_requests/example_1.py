#!/usr/bin/python
"""
Purpose:
    downloading a web page

    pip install requests
"""

import requests

response = requests.get("https://www.timeanddate.com/worldclock/india/new-delhi")
# print(response.text)
with open("content.html", "wb") as f:
    f.write(response.text.encode("utf-8"))
    f.close()
