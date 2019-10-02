#!/usr/bin/python
import re

reg = re.compile('(.*)[|]')
f = open("file1.txt")
g = open("file2.txt", 'a')
f_string = f.read()
g.writelines(reg.findall(f_string))
g.close()
f.close()
