#!/usr/bin/python
"""
XML parsing: 

"""
import untangle

obj = untangle.parse('books.xml')
print(obj)

print(dir(obj))

print(obj.catalog.book)
