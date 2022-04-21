#!/usr/bin/python
"""
Purpose: Web scrapping
"""
import re


hrefs = []
with open("rediff.html", "r") as f:
    file_content = f.readlines()

    for each_line in file_content:
        if "href" in each_line:
            result = re.search('href="https://(.*)("\s)?', each_line)
            if result:
                # print(result.group())
                hrefs.append(result.groups(1)[0] + "\n")

with open("rediff_hrefs.txt", "w") as g:
    hrefs = sorted(hrefs, key=lambda x: len(x))
    g.writelines(hrefs)
    g.close()
