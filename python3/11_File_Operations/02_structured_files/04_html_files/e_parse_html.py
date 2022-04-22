#!/usr/bin/python
"""
Purpose: HtML parsing, using lxml
    - lxml has simple syntax and faster in performance
"""
import requests
from lxml import html

page = requests.get("https://html.com/")
tree = html.fromstring(page.content)

with open("html_webpage.html", mode="w", encoding="utf-8") as f:
    f.write(tree.text_content())
