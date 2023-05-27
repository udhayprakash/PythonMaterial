#!/usr/bin/python
"""
Purpose: GZip File operations
"""
import gzip

# Compress the file
fp = open("zen.txt", "rb")
data = fp.read()
bindata = bytearray(data)
with gzip.open("zen.txt.gz", "wb") as f:
    f.write(bindata)

# uncompressed file from gzip archive
fp = open("zen1.txt", "wb")
with gzip.open("zen.txt.gz", "rb") as f:
    bindata = f.read()
    fp.write(bindata)
    fp.close()
print()

# ----------------
f = gzip.GzipFile("testnew.txt.gz", "wb")
data = b"Python - Batteries included"
f.write(data)
f.close()

f = gzip.GzipFile("testnew.txt.gz", "rb")
data = f.read()
print(data)  # b'Python - Batteries included'
