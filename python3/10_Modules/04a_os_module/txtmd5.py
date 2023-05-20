import hashlib
import os
from os.path import join

hashes = dict()
for dirname, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".txt"):
            thefile = os.path.join(dirname, filename)
            fhand = open(thefile, "r")
            data = fhand.read()
            fhand.close()
            hash = hashlib.md5(data.encode("utf-8")).hexdigest()
            # print(thefile, hash)
            if hash in hashes:
                print(hashes[hash], thefile)
            else:
                hashes[hash] = thefile
