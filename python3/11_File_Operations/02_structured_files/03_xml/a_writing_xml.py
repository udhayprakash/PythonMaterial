#!/usr/bin/python
"""
Purpose: writing an XML file
"""
from xml.etree.ElementTree import Element, SubElement, tostring

root = Element('root')

child = SubElement(root, 'child')
child.text = 'I am a child'

# To a xml string
print(tostring(root))
result_str = tostring(root).decode('utf-8')
print(result_str)

# To a xml file
with open('first.xml', 'w') as f:
    f.write(result_str)