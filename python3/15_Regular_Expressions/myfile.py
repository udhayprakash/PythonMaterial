import re

with open('myfile.txt') as fh:
    file_content = fh.read()
    print(file_content)
    fh.close()