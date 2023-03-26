#!/usr/bin/python
"""
Purpose: scraping
"""
import lxml.html
import requests

res = requests.get("https://pydata.org/nyc2018/schedule/")
print(res.status_code)
print(res.text)
tree = lxml.html.fromstring(res.text)
for tr in tree.xpath('//span[@class="speaker"]'):
    name = tr.xpath("text()")
    url = tr.xpath("@href")

    print(name)
    print(url)
