#!/usr/bin/python
"""
Purpose: writing an XML file
    XML - eXtensible Markup Language
        - designed to store and transport data. 
        - often used for distributing data over the 
           Internet(especial in web development).

XML vs HTML 
    XML : is used to store or transport data. So the XML is a Complement to HTML.
    HTML: is used to format and display the same data.

- XML Tags are Case Sensitive
- All XML Elements Must Have a Closeing Tag
    <p>This is a paragraph.</p>
    <br />  <!-- This is a self closing -->
- XML Attribute Values Must Always be Quoted

"""
from xml.etree.ElementTree import Element, SubElement, tostring

root = Element('root')

child = SubElement(root, 'child')
child.text = 'I am a child'

child2 = SubElement(root, 'child2')

# To a xml string
# print(tostring(root))
result_str = tostring(root).decode('utf-8')
print(result_str)

# To a xml file
with open('first.xml', 'w') as f:
    f.write(result_str)