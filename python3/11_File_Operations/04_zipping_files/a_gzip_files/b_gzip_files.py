import gzip

# compress a gzip file
input_fh = open("/Users/joe/xxtest", "rb")
s = input_fh.read()
input_fh.close()

output = gzip.GzipFile("/Users/joe/xxtest.gz", "wb")
output.write(s)
output.close()

print("done")


# ----------------------------------------
# decompress a gzip file
input_fh = gzip.GzipFile("/Users/joe/xxtest.gz", "rb")
s = input_fh.read()
input_fh.close()

output = open("/Users/joe/xxtest", "wb")
output.write(s)
output.close()

print("done")
