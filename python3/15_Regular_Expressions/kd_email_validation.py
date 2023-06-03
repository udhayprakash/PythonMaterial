"""
purpose: regular expression

Ex: email ids
"""

import re

print(
    re.findall(
        r"\S+@\S+",
        "This message from csev@umich.edu to cwen@iupui.edu is about a meeting @2PM",
    )
)

email_ids = """
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
SUPPORT@microsoft.com
"""
print(re.findall(r"\S+@\S+", email_ids))

# print(re.findall(  "[a-z]+@[a-z]+\.[a-z]+",  email_ids))
# print(re.findall(  "[a-z.]+@[a-z.]+\.[a-z]+",  email_ids))
# print(re.findall(  "[a-z._]+@[a-z._]+\.[a-z_]+",  email_ids))
print(re.findall("[a-zA-Z._]+@[a-zA-Z._]+\.[a-zA-Z_]+", email_ids))

# Assignment:
# 1. FInd all the valid Phone numbers in the given target string
