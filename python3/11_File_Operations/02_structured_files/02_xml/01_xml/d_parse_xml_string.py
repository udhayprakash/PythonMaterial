"""
Purpose: To parse(read) xml string
"""
import defusedxml.ElementTree

input_string = """
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
</stuff>"""

stuff_tree = defusedxml.ElementTree.fromstring(input_string)

nodes = stuff_tree.findall("users")  # child level
print(nodes)

nodes = stuff_tree.findall("user")  # cant find in child level
print(nodes)

nodes = stuff_tree.findall("users/user")  # to check in subchild level
print(nodes)
print("User count:", len(nodes))


for item in nodes:
    print("\nName", item.find("name").text)
    print("Id", item.find("id").text)
    print("Attribute", item.get("x"))
