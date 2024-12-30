"""
purpose: XML to python DICT conversion

    pip install xmltodict
"""

import xmltodict
from pprint import pp



with open('books.xml', 'r') as fh:
    file_content = fh.read()

doc = xmltodict.parse(file_content)
pp(doc)

mapping = {}
for each in doc["catalog"]["book"]:
    mapping[each["@isbn"]] = each["title"]

pp(mapping)


# Assignment:  explore how to convert the dict ,
# back to xml using this xmltodict module.. Hint: unparse()
