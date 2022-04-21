#!/usr/bin/python3
"""
Purpose: Reading(Parsing) XML
"""
from xml.etree.ElementTree import parse
from pprint import pprint

tree = parse("books.xml")

# To check for presence of a particular tag in xml file
# print(f"{tree.findall('book') =}")
print()

books = {}
for each in tree.findall("book"):
    isbn = each.attrib["isbn"]
    for ech_sub in each.findall("title"):
        book_title = ech_sub.text
        books[isbn] = book_title
# print(dir(each))

pprint(books)

# Assignment: Enhance it by changing the values of books dict
# as a tuple containing book_title, author and date

{"0-596-00128-2": ("Python & XML", "Jones, Drake", "December 2001")}
