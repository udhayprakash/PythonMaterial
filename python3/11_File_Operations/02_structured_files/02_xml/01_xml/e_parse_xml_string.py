#!/usr/bin/python3

import defusedxml.ElementTree

data = """
<person>
  <name>Gudo Van Russum</name>
  <phone type="intl">
     +1 734 808 5456
   </phone>
   <email hide="yes"/>
</person>"""

tree = defusedxml.ElementTree.fromstring(data)
print("Name:", tree.find("name").text)
print("Attr:", tree.find("email").get("hide"))
