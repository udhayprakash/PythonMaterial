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

import xml

# print(dir(xml))

import xml.etree.ElementTree as ET
from xml.dom import minidom

# print(dir(ET))


root  = ET.Element("root")

child = ET.SubElement(root, "child")
child.text = "I am a child"

child2 = ET.SubElement(root, "child2")
# child2.text = "I am second child"

# To display the xml string
result_str = ET.tostring(root)
print(result_str)
# b'<root><child>I am a child</child><child2>I am second child</child2></root>'
print()


result_str2 = minidom.parseString(
    ET.tostring(root)
).toprettyxml()

print(result_str2)


# <?xml version="1.0" ?>
# <root>
#         <child>I am a child</child>
#         <child2>I am second child</child2>
# </root>




# <?xml version="1.0" ?>
# <root>
#         <child>I am a child</child>
#         <child2/>
# </root>


# writing to file 
with open('a_write_xml.xml', 'w') as fh:
    fh.write(result_str2)

