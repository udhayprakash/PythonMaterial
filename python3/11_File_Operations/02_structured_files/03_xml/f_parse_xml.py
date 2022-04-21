#!/usr/bin/python
"""
Purpose: Reading(Parsing) XML
"""
from pprint import pprint

try:
    import untangle
except ModuleNotFoundError as ex:
    print(repr(ex))
    from os import system

    system("pip install untangle --user")
    import untangle

obj = untangle.parse("books.xml")
# print(obj)
# print(dir(obj))

# print(obj.catalog)
# print(dir(obj.catalog))
# print(obj.catalog.book)

mapping = {}
for each in obj.catalog.book:
    # print(each)
    # print(each.attrib['isbn'])
    isbn = each.get_attribute("isbn")
    title = each.title.cdata
    mapping[isbn] = title

pprint(mapping)
