from lxml import etree

# create XML
root = etree.Element('root')
child1 = etree.Element('child1')
root.append(child1)

# another child with text
child2 = etree.Element('child2')
child2.text = 'some text'
root.append(child2)
child1.append(child2)


# pretty string
s = etree.tostring(root, pretty_print=True)
print s