#!/usr/bin/python
"""
purpose: regular expression  demo 

Ex: email ids
"""

import re 

email_ids = '''
Edit the Expression & Text to see matches. Roll over matches or the expression for details. Und
python@programm.com
Sample text for testing:
abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\/|<>"'python@gmail.com
12345 -98.7 3.141 .6180 9,000 +42
555.123.4567 +1-(800)-555-2468
foo@demo.net bar.ba@test.co.uk
www.demo.com http://foo.co.uk/
http://regexr.com/foo.html?q=bar
https://mediatemple.net
mediatepmple@outlook.com
mubeen.tom@hacker.com
1%453&harini_new@in.com
'''

matched_emails  = re.findall('[a-zA-Z0-9._]+@[a-zA-Z0-9._]+', email_ids)

for each_email in matched_emails:
    print(each_email)