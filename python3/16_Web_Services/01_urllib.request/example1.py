#!/usr/bin/python
import urllib.request

url = 'https://developer.yahoo.com/'
u = urllib.request.urlopen(url)
# u is a file-like object
data = u.read()
f = open('yahooData.txt', 'ab+')

f.write(data)
f.close()

