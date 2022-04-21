#!/usr/bin/python
"""
Purpose: creating html using lxml
    - lxml has simple syntax and faster in performance
"""

from lxml import etree

root_elem = etree.Element('html')

etree.SubElement(root_elem, 'head')
etree.SubElement(root_elem, 'title')
etree.SubElement(root_elem, 'body')

print(etree.tostring(root_elem, pretty_print=True).decode('utf-8'))

# These html elements can be accessed as a list

html = root_elem[0]
print(f'{html.tag                   =}')

for element in root_elem:
    print(f'{element.tag                =}')

# .iselement - to check if given element is a valid HTML element
print(f'{etree.iselement(root_elem) =}')
