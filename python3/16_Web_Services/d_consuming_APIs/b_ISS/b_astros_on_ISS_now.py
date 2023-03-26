#!/usr/bin/python
"""
Purpose: To get the Astronomers living in ISS now

    http://api.open-notify.org/astros.json
"""

import sys
from pprint import pp

import requests

response = requests.get("http://api.open-notify.org/astros.json")
# print(dir(response))
print(f"{response.status_code =}")
print(f"{response.url         =}")
print(f"{response.reason      =}")
print(f"{response.ok          =}")
print(f"{response.is_redirect =}")
print(f"{response.is_permanent_redirect =}")
print(f"{response.elapsed    =}")

# pp(dict(response.headers))
print()
# Method 1
# response_content = str(response.content, 'utf-8')
# response_content = json.loads(response_content)
# print(response_content)

# Method 2:
if response.headers["Content-Type"] != "application/json":
    print("Error: Content-Type is not application/json")
    sys.exit()


response_content = response.json()
pp(response_content)

number = response_content["number"]

crafts = set()
astros = []

for each_record in response_content["people"]:
    craft = each_record["craft"]
    name = each_record["name"]
    crafts.add(craft)
    astros.append(name)

print(
    f"""
    CRAFTs               : {crafts}
    No. Of ASTRONOMERS  : {number}
    Names of Astronomers: {astros}
"""
)
