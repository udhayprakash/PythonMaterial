#!/usr/bin/python
"""
Purpose: XML to python DICT conversion
"""
from pprint import pprint

try:
    import xmltodict
except ModuleNotFoundError as ex:
    print(repr(ex))
    from os import system

    system('pip install xmltodict --user')
    import xmltodict

with open('books.xml', 'r') as fh:
    file_content = fh.read()
    doc = xmltodict.parse(file_content)
    pprint(doc)

    mapping = {}
    for each in doc['catalog']['book']:
        mapping[each['@isbn']] = each['title']

    pprint(mapping)

# Assignment:  explore how to convert the dict ,
# back to xml using this xmltodict module.. Hint: unparse()
