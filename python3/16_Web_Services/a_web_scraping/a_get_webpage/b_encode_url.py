#!/usr/bin/python
"""
Purpose: Encode URL
    Some character in URL needs to be encoded, such as NON-ASCII character. 
    You can use the quote function to encode them.

"""

# from urllib import quote  # Python 2.X

from urllib.parse import quote  # Python 3.X

print(quote("~What's your father's last name?"))
#            ~What%27s%20your%20father%27s%20last%20name%3F

print('http://www.google.com/search?q=' + quote("ménage à trois"))
# http://www.google.com/search?q=m%C3%A9nage%20%C3%A0%20trois
