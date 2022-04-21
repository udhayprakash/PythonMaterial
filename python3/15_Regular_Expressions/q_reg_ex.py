#!/usr/bin/python3
"""
Purpose: regular expression

\d - presence of any digit 0-9
\D - absence of any digit
\w - presence of any alphanumeric a-z A-Z 0-9
\W - absence of any alphanumeric
\s  -presence of  white space AND \n
\S  - absence of white space and \n

. (re operator) -> to get any character
To escape any re operator in pattern, place a \ before it, or enclose in []
"""

import re

# identify decimal number
print()
# ['12', '21323', '3', '23432', '234', '23', '234324', '0', '000003243']

# only floating point values
print(re.findall(r"\d+.\d+", "12 21323.3 23432.234 23.234324 -0.000003243"))
# ['12 21323', '3 23432', '234 23', '234324', '0.000003243']

print(re.findall(r"\d+\.\d+", "12 21323.3 23432.234 23.234324 -0.000003243"))
# ['21323.3', '23432.234', '23.234324', '0.000003243']

print(re.findall(r"\d+[.]\d+", "12 21323.3 23432.234 23.234324 -0.000003243"))
# ['21323.3', '23432.234', '23.234324', '0.000003243']

# both integer and floating point values
print(re.findall(r"\d+\.?\d+", "12 21323.3 23432.234 23.234324 -0.000003243"))
# ['12', '21323.3', '23432.234', '23.234324', '0.000003243']

print(re.findall(r"\d+[.]?\d+", "12 21323.3 23432.234 23.234324 -0.000003243"))
# ['12', '21323.3', '23432.234', '23.234324', '0.000003243']
