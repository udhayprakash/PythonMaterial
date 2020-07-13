#!/usr/bin/python
"""
Purpose: HtML parsing, using lxml
    - lxml has simple syntax and faster in performance
"""
from lxml import html
import requests

page = requests.get('https://html.com/')
tree = html.fromstring(page.content)

with open('html_webpage.html', mode='w', encoding='utf-8') as f:
    f.write(tree.text_content())