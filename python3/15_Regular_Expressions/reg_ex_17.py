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

# identify decimal number 
print(re.findall('\d+', '12 21323.3 23432.234 23.234324 -0.000003243'))

# only floating point values 
print(re.findall('\d+\.\d+', '12 21323.3 23432.234 23.234324 -0.000003243'))

# both integer and floating point values 
print(re.findall('\d+\.?\d+', '12 21323.3 23432.234 23.234324 -0.000003243'))
