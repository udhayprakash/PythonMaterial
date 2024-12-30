"""
Purpose: write xml file using lxml module
"""
try:
    from lxml import etree
except ModuleNotFoundError as ex:
    print(repr(ex))
    from os import system

    system("pip install lxml")
    from lxml import etree



# creating the XML
root = etree.Element("root")

child1 = etree.Element("child1")
root.append(child1)


# another child with text
child2 = etree.Element("child2")
child2.text = "some text"


root.append(child2)
# child1.append(child2)


xml_Str = etree.tostring(root)
print(xml_Str)
# b'<root><child1/><child2>some text</child2></root>'

xml_Str = etree.tostring(root, pretty_print=True)
print(xml_Str.decode('utf-8'))

# <root>
#   <child1/>
#   <child2>some text</child2>
# </root>


# <root>
#   <child1>
#     <child2>some text</child2>
#   </child1>
# </root>
