#!/usr/bin/python
"""
Purpose: XML to dict conversion  

"""
import xmltodict
from pprint import pprint 

with open('books.xml') as fh:
    doc = xmltodict.parse(fh.read())
    pprint(doc)
    for each_book in doc['catalog']['book']:
        print(each_book['title'])



# Assignment:  explore how to convert the dict , 
# back to xml using this xmltodict module.. Hint: unparse()