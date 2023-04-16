#!/usr/bin/python
"""
Purpose: To get the current location of ISS

    http://api.open-notify.org/iss-now.json

"""
import sys
from pprint import pp

import requests

response = requests.get("http://api.open-notify.org/iss-now.json", timeout=5)
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
# pp(response_content)

latitude = response_content["iss_position"]["latitude"]
longitude = response_content["iss_position"]["longitude"]

print(
    f"""ISS CURRENT LOCATION:
            LATITUDE : {latitude}
            LONGITUDE: {longitude}"""
)
