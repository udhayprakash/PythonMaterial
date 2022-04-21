#!/usr/bin/env python

import re
string = 'foo foobar'

reg = re.compile('foobar$')
print reg.match(string)
print reg.search(string)
print reg.search(string).group()
