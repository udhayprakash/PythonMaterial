#!/usr/bin/python
"""
purpose: regular expression  demo 

\d - presence of any digit 0-9 
\D - absence of any digit 
\w - presence of any alphanumeric a-z A-Z 0-9
\W - absence of any alphanumeric
\s  -presence of  white space AND \n 
\S  - absence of white space and \n
"""

import re 
print(re.search('[a-z]+', 'Udhay Prakash').group())
print(re.search('\w+', 'Udhay Prakash').group())

print(re.search('\w+\W\w+', 'Udhay Prakash').group())

print(re.search('(\w+)\W(\w+)', 'Udhay Prakash').group())
print(re.search('(\w+)\W(\w+)', 'Udhay Prakash').group(0))
                #  1      2 
print(re.search('(\w+)\W(\w+)', 'Udhay Prakash').group(1))
print(re.search('(\w+)\W(\w+)', 'Udhay Prakash').group(2))

print(re.search('(\w+)\W(\w+)', 'Udhay Prakash').groups())
