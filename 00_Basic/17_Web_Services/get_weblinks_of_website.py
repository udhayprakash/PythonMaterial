import urllib
import lxml.html
connection = urllib.urlopen('https://www.stackoverflow.com')

data = connection.read()

dom =  lxml.html.fromstring(data)

print dom

for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
    print link
