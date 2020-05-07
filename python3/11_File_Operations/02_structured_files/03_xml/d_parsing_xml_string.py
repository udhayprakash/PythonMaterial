#!/usr/bin/python
"""
Purpose: To parse(read) xml string
"""
import xml.etree.ElementTree as ElementTree

input_string = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Udhay</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Prakash</name>
        </user>
    </users>
</stuff>'''

stuff = ElementTree.fromstring(input_string)
nodes = stuff.findall('users/user')
print('User count:', len(nodes))

# print(nodes)
for item in nodes:
    print('\nName', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
