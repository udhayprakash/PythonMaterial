#!/usr/bin/python
"""
purpose: regular expression  demo 

pearl based regex grouping 
PCRE - pearl compatible regular expression 

"""

import re 

# ip address validation 

# pattern = '[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}'
pattern = '[0-2][0-9][0-9]\.[0-2][0-9][0-9]\.[0-2][0-9][0-9]\.[0-2][0-9][0-9]'

with open('ip_addresses_info.txt') as fh:
    ip_addresses = fh.read()
    print(ip_addresses)

    print(re.findall(pattern, ip_addresses))
    fh.close()