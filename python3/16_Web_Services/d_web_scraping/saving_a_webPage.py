import sys
import urllib

f = urllib.urlopen("http://www.google.com")
g = open("newFile.html", "w+b")
while 1:
    buf = f.read(2048)
    if not len(buf):
        break
    g.write(buf)
    sys.stdout.write(buf)
