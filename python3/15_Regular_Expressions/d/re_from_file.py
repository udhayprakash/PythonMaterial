#!/usr/bin/env python

import re

reg = re.compile('This', re.M)

with open('example.html', 'rb') as searchFile:
	searchData = searchFile.readlines()
	temp = reg.search(str(searchData)).group()
	print temp
	with open('searchResults.txt', 'a+b') as resultFile:
		resultFile.write(temp)
	
resultFile.close()
searchFile.close()
