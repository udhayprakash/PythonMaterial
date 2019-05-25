#!/usr/bin/python
"""
Purpose: HtML parsing
"""
from lxml import html 
import requests 

page = requests.get('https://www.bseindia.com/markets/Equity/newsensexstream.aspx')
tree = html.fromstring(page.content)