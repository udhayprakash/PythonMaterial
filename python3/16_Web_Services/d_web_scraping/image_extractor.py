#!usr/bin/env python
import re
import urllib.error
import urllib.parse
import urllib.request

print("The URL crawler starts..")
myurl = "http://www.sliit.lk/"
x = 1
urlcontent = urllib.request.urlopen(myurl).read()
imgUrls = re.findall('img .*?src="(.*?)"', urlcontent)
for imgUrl in imgUrls:
    img = imgUrl
    print(img)
    urllib.request.urlretrieve(img, str(x) + ".jpg")
    x = x + 1
