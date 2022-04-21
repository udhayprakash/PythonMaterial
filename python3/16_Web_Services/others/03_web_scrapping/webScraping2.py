import re
import urllib

urls = ["http://google.com", "http://nytimes", "http://CNN.com"]

regex = "<title>(.+?)</title>"
pattern = re.compile(regex)

i = 0
while i < len(urls):
    htmlfile = urllib.urlopen(urls[i])
    htmltext = htmlfile.read()
    titles = re.findall(pattern, htmltext)
    print(titles)
    print(htmltext[0:100])
    i += 1
