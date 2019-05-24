#!/usr/bin/python
"""
purpose: regular expression  demo 

patterns 
    *  previous character can occur 0 or more times
    +  previous character can occur 1 or more times
    ?  previous character can occur 0 or 1 time only 
"""

import re 


print(re.search('a.?', 'a').group())           # b is occuring 0 times
print(re.search('a.?', 'ab').group())          # b is occuring 1 times
print(re.search('a.?', 'abb').group())         # b is occuring 2 times
print(re.search('a.?', 'abbb').group())        # b is occuring 3 times

# print(re.search('a.?', 'bbbbbbb').group())     # a is occurring 0 times
print(re.search('a?.?', 'bbbbbbb').group())     # a is occurring 0 times


# print(re.search('a.+', 'a').group())           # b is occuring 0 times
print(re.search('a.+', 'ab').group())          # b is occuring 1 times
print(re.search('a.+', 'abb').group())         # b is occuring 2 times
print(re.search('a.+', 'abbb').group())        # b is occuring 3 times

# print(re.search('a.+', 'bbbbbbb').group())     # a is occurring 0 times
# print(re.search('a+.+', 'bbbbbbb').group())     # a is occurring 0 times
