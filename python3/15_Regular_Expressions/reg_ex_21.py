#!/usr/bin/python
"""
purpose: regular expression  demo

application  of regex flags
    re.I (re.IGNORECASE)--> for case-sensitive search/match
    re.S (re.DOTALL)    --> to include newline character for . operator

    . to get any character except newline
"""

import re

string = 'Today is Friday.\n Tomorrow is morning'
print(re.findall('.*', string))

print(re.search('.*', string).group())

print(re.search('.*', string, re.DOTALL).group())  # re.S
print(re.search('.*', string, re.S).group())

print(re.search('Today.*', string, re.S).group())

# print(re.search('today.*', string, re.S).group())
print(re.search('today.*', string, re.I).group())

# applying more than one flag
print(re.search('today.*', string, re.I|re.S).group())
