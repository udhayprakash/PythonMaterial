#!/usr/bin/python
"""
purpose: regular expression  demo 

greedy patterns 
    .*
"""

import re

print(re.search('', '<h1>name</h1>').group())

print(re.search('<h1>', '<h1>name</h1>').group())

print(re.search('<..>', '<h1>name</h1>').group())

# greedy pattern 
print(re.search('<.*>', '<h1>name</h1>').group())
# non greedy pattern
print(re.search('<.*?>', '<h1>name</h1>').group())

print(re.search('.*', '').group())
print(re.search('.*', 'aS').group())
print(re.search('.*', 'ASDASDSADS').group())
print(re.search('.*', 'ASDASDSADS 3444 *&(*&(_)_.dfaderrrerq').group())

print(re.search('.*', '').group())  # anychar occured 0 timess
# print(re.search('.+', '').group())  # anychar occuured 0 times
print(re.search('.+', 'c').group())  # anychar occuured 1 times
