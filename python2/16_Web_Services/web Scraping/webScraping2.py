import urllib
import re

urls = ["http://google.com", "http://nytimes", "http://CNN.com"]

i=0

regex = '<title>(.+?)</title>'
pattern = re.compile(regex)
while i<len(urls):
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	titles = re.findall(pattern, htmltext)
	print titles
	print htmltext[0:100]
	i+=1