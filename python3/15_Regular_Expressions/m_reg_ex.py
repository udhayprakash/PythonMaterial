#!/usr/bin/python3
"""
purpose: regular expressions

patterns
    *  previous character can occur 0 or more times
    +  previous character can occur 1 or more times
    ?  previous character can occur 0 or 1 time only

    . To get any character
"""

import re

# NON- Greedy patterns
# .? Any character( except newline) can occur  0 or 1 time only
print(re.search('a.?', 'a').group())  # b is occurring 0 times
print(re.search('a.?', 'ab').group())  # b is occurring 1 times
print(re.search('a.?', 'abb').group())  # b is occurring 2 times
print(re.search('a.?', 'abbb').group())  # b is occurring 3 times

print(re.search('a.?', 'a').group())
print(re.search('a.?', 'ar').group())  # r is occurring 1 times
print(re.search('a.?', 'amm').group())
print(re.search('a.?', 'ank').group())

# print(re.search('a.?', 'bbbbbbb').group())     # a is occurring 0 times
print(re.search('a?.?', 'bbbbbbb').group())  # a is occurring 0 times
print()


# GREEDY searches/matches

# .+  Any character( except newline) can occur  1 or any no. of time
# print(re.search('a.+', 'a').group())  # b is occurring 0 times
print(re.search('a.+', 'ab').group())  # b is occurring 1 times
print(re.search('a.+', 'abb').group())  # b is occurring 2 times
print(re.search('a.+', 'abbb').group())  # b is occurring 3 times

# print(re.search('a.+', 'bbbbbbb').group())     # a is occurring 0 times
# print(re.search('a+.+', 'bbbbbbb').group())     # a is occurring 0 times
