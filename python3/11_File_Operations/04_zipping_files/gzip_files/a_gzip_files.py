#!/usr/bin/python
"""
Purpose: GZip File operations
    - GZip application is used for compression and decompression of files.
    - The gzip data compression algorithm itself is based on zlib module.
    - Modes of file operation
        binary mode: 'r', 'rb', 'a', 'ab', 'w', 'wb', 'x', 'xb'
        text mode : 'rt', 'at', 'wt', or 'xt'

"""
import gzip

print(gzip.__doc__)
print()

# compression and save in file
original_data = b'Python - Batteries included'
print(f'{original_data  =}')
with gzip.open('test.txt.gz', 'wb') as f:
    f.write(original_data)

# Decompression and retrieving data
with gzip.open('test.txt.gz', 'rb') as f:
    decrypted_data = f.read()
    print(f'{decrypted_data =}')


# --------------------------------
# Compress the file
fp = open('zen.txt', 'rb')
data = fp.read()
bindata = bytearray(data)
with gzip.open('zen.txt.gz', 'wb') as f:
    f.write(bindata)

# uncompressed file from gzip archive
fp = open('zen1.txt', 'wb')
with gzip.open('zen.txt.gz', 'rb') as f:
    bindata = f.read()
    fp.write(bindata)
    fp.close()


# ----------------
f = gzip.GzipFile('testnew.txt.gz', 'wb')
data = b'Python - Batteries included'
f.write(data)
f.close()

f = gzip.GzipFile('testnew.txt.gz', 'rb')
data = f.read()
print(data)  # b'Python - Batteries included'
