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
