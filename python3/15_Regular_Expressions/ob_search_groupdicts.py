"""
purpose: regular expression

pearl based regex grouping
PCRE - pearl compatible regular expression

"""

import re

print(re.search(r"(\w*) (\w*)", "udhay prakash").group())
print(re.search(r"(\w*) (\w*)", "udhay prakash").group(0))
# group index      1      2

print(re.search(r"(\w*) (\w*)", "udhay prakash").group(1))  # udhay
print(re.search(r"(\w*) (\w*)", "udhay prakash").group(2))  # prakash

print(re.search(r"(\w*) (\w*)", "udhay prakash").groups())  # ('udhay', 'prakash')
print()

#  (?P<name>)
print(re.search(r"(?P<first>\w+) (?P<last>\w+)", "Udhay Prakash").group("first"))
print(re.search(r"(?P<first>\w+) (?P<last>\w+)", "Udhay Prakash").group("last"))

print(re.search(r"(?P<first>\w+) (?P<last>\w+)", "Udhay Prakash").groupdict())
# {'first': 'Udhay', 'last': 'Prakash'}
