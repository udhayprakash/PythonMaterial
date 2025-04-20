"""
Purpose: Reading(Parsing) XML
"""
from pprint import pp
import defusedxml.ElementTree

tree = defusedxml.ElementTree.parse("books.xml")

# print(dir(tree))

# To check for presence of a particular tag in xml file
# print(tree.find('book'))
# print(tree.findall('book'))
# print()

books = {}
for each in tree.findall('book'):
    isbn= each.attrib['isbn']
    for each_sub in each.findall('title'):
        book_title = each_sub.text
        books[isbn] = book_title

pp(books)
