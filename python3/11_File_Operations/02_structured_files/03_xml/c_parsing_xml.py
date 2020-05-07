#!/usr/bin/python
"""
Purpose: Reading(Parsing) XML
"""
from xml.etree.ElementTree import parse
from pprint import pprint
tree = parse('books.xml')

# print(tree.findall('book'))
books = {}
for each in tree.findall('book'):
    isbn = each.attrib['isbn']
    for ech in  each.findall('title'):
        title = ech.text
        books[isbn] = title

pprint(books)


# Assignment: Enhance it by changing the values of books dict 
# as a tuple containing book_title, author and date