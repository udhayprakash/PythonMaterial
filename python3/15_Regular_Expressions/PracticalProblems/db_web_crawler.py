import re

import requests

# get url
# url = input("Enter a URL (include `http://`): ")
url = "https://stackoverflow.com"

# connect to the url
website = requests.get(url)

# read html
html = website.text

# use re.findall to grab all the links
links = re.findall(r'"((http|ftp)s?://.*?)"', html)
emails = re.findall(r"([\w\.,]+@[\w\.,]+\.\w+)", html)

# print the number of links in the list
print("\nFound {} links".format(len(links)))
for email in emails:
    print(email)
