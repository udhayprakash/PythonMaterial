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

target_string = '''
Hi everyone!
The PARTY is on 23rd of May 2019, at xyz place. at time 7.30 pm IST
And the RECEPTION is on 30th of Mat, 2019 at xxx place.
Thanks
'''

print(re.findall('\w+', target_string))
print(re.findall('\W+', target_string))
print()
print(re.findall('\s+', target_string))
print(re.findall('\S+', target_string))
