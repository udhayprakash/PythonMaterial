import urllib

htmlfile = urllib.urlopen('http://google.com')

htmltext = htmlfile.read()

print htmltext
