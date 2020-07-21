# compress a gzip file

import gzip

input = open("/Users/joe/xxtest", 'rb')
s = input.read()
input.close()

output = gzip.GzipFile("/Users/joe/xxtest.gz", 'wb')
output.write(s)
output.close()

print("done")



# ----------------------------------------
# decompress a gzip file

import gzip

input = gzip.GzipFile("/Users/joe/xxtest.gz", 'rb')
s = input.read()
input.close()

output = open("/Users/joe/xxtest", 'wb')
output.write(s)
output.close()

print("done")