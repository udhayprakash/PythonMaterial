#!/usr/bin/python
"""
Purpose: Get my Public IP address
"""
import urllib.request

connection = urllib.request.urlopen('http://checkip.dyndns.org')

print(f'''
    {connection.url         = }
    {connection.status      = }
    {connection.length      = }
''')

content = connection.read()
# print(f'{type(content) =}')

content = content.decode('utf-8')
print(f'{type(content) =}')

print(content)

# Method 1
# print(content.split('Current IP Address: ')[1])
my_public_ip = content.split('Current IP Address: ')[1].split('</body>')[0]
print("My Public IP Address is: ", my_public_ip)


# Method 2 - Using Regular Expressions
import re 
my_public_ip = re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", content)[0]
print("My Public IP Address is: ", my_public_ip)