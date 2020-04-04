#!/usr/bin/python
"""
purpose: regular expression  demo 

pearl based regex grouping 
PCRE - pearl compatible regular expression 

"""

import re

print(re.search('(\w*) (\w*)', 'udhay prakash').group())
print(re.search('(\w*) (\w*)', 'udhay prakash').group(0))

# group index      1      2
print(re.search('(\w*) (\w*)', 'udhay prakash').group(1))
print(re.search('(\w*) (\w*)', 'udhay prakash').group(2))

print(re.search('(\w*) (\w*)', 'udhay prakash').groups())

#  (?P<name>)
print(re.search(r"(?P<first>\w+) (?P<last>\w+)", "Udhay Prakash").group('first'))
print(re.search(r"(?P<first>\w+) (?P<last>\w+)", "Udhay Prakash").group('last'))

print(re.search(r"(?P<first>\w+) (?P<last>\w+)", "Udhay Prakash").groupdict())
