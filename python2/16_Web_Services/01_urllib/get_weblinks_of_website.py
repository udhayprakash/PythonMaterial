import urllib

import lxml.html

connection = urllib.urlopen('https://www.stackoverflow.com')

data = connection.read()

with open('stackoverflow.html', 'wb') as f:
    f.write(data)
    f.close()

dom = lxml.html.fromstring(data)

print dom

for link in dom.xpath('//a/@href'):  # select the url in href for all a tags(links)
    if str(link).startswith('https'):
        print link
