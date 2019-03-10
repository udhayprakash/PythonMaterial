

import urllib

url = 'https://developer.yahoo.com/'
u = urllib.urlopen(url)
# u is a file-like object
data = u.read()
f = open('yahooData.txt', 'ab+')

f.write(data)
f.close()

