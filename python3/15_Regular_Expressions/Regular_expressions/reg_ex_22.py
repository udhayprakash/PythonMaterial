#!/usr/bin/python
"""
purpose: regular expression  demo 

application  of regex flags
"""

import re 


string = 'Today is Friday.\n Tomarrow is morning'
print(re.findall('.*', string))

print(re.search('.*', string).group())

print(re.search('.*', string, re.DOTALL).group() ) #re.S
print(re.search('.*', string, re.S).group() ) 


print(re.search('Today.*', string, re.S).group() ) 
# applying more than one flag 
print(re.search('today.*', string, re.S|re.I).group() ) 
