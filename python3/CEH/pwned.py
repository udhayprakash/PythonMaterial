#!/usr/bin/python
"""
Purpose:

pwnedAPI
========

Python API for http://haveibeenpwned.com
Checks if an email is in a recently released password dump.

Usage
-----
To check a single email:
```
from pwned import check
check('troyhunt@hotmail.com')
```
To check multiple emails at once:
```
check(['troyhunt@hotmail.com','example@example.com'])
```
The result is returned as a dictionary.
To run as a standalone script pass the emails as variables"
```shell
python pwned.py troyhunt@hotmail.com
```
"""

from urllib2 import urlopen
import json
import sys


def check(emails):
    if type(emails) is str:
        emails = [emails]
    dic = {}
    for email in emails:
        em = email.replace("@", "%40")
        try:
            raw = urlopen('http://haveibeenpwned.com/api/breachedaccount/' + em)
            data = raw.read()
            info = json.loads(data)
            for i in range(len(info)):
                info[i] = info[i].encode('ascii')
            dic.update({email: info})
        except:
            dic.update({email: 'None'})
    return dic


if __name__ == "__main__":
    length = len(sys.argv) - 1
    for i in range(length):
        print(check(sys.argv[i + 1]))
