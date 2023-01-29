import urllib.error
import urllib.parse
import urllib.request

htmlfile = urllib.request.urlopen("http://google.com")

htmltext = htmlfile.read()

print(htmltext)
