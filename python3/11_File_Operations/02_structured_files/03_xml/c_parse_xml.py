#!/usr/bin/python
"""
Purpose: Reading(Parsing) XML
"""
from xml.etree.ElementTree import parse
from pprint import pprint
tree = parse('books.xml')

mapping = {}
for B in tree.findall('book'):
    isbn = B.attrib['isbn']
    for T in B.findall('title'):
        # print(isbn, T.text)
        mapping[isbn] = T.text

pprint(mapping)