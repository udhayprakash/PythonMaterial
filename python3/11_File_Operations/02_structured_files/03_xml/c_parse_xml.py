#!/usr/bin/python
"""
Purpose: Reading(Parsing) XML
"""
from xml.etree.ElementTree import parse
from pprint import pprint

tree = parse('books.xml')

# To check for presence of a particular tag in xml file
print(f"{tree.findall('book') =}")
print()

books = {}
for each in tree.findall('book'):
    isbn = each.attrib['isbn']
    for ech in each.findall('title'):
        title = ech.text
        books[isbn] = title

pprint(books)


# Assignment: Enhance it by changing the values of books dict 
# as a tuple containing book_title, author and date