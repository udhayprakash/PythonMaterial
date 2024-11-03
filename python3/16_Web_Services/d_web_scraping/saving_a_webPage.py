import sys
import urllib

f = urllib.urlopen("http://www.google.com")
with open("newFile.html", "w+b") as g:
    while 1:
        buf = f.read(2048)
        if not len(buf):
            break
        g.write(buf)
        sys.stdout.write(buf)
