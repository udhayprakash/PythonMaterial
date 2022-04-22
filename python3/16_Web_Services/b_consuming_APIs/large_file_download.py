#!/usr/bin/python3
"""
Purpose: Downloading Large data files
"""
import urllib.error
import urllib.parse
import urllib.request

url = "http://download.thinkbroadband.com/10MB.zip"

file_name = url.split("/")[-1]
req = urllib.request.Request(url)
req.add_header("User-agent", "Internet Explorer/2.0")
url_handler = urllib.request.urlopen(req)

f = open(file_name, "wb")
meta = url_handler.info()
file_size = int(meta.getheaders("Content-Length")[0])
print("Downloading: %s Bytes: %s" % (file_name, file_size))


file_size_dl = 0
block_sz = 8192
while True:
    buffer = url_handler.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100.0 / file_size)
    status = status + chr(8) * (len(status) + 1)
    print(status, end=" ")

f.close()
