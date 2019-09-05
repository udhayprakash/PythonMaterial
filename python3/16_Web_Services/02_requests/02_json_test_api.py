#!/usr/bin/python
"""
Purpose: To demonstrate the usage of API 

https://jsonplaceholder.typicode.com/
"""
from pprint import pprint

import requests

# URL = 'https://jsonplaceholder.typicode.com/posts'
# URL = 'https://jsonplaceholder.typicode.com/posts/1'
URL = 'https://jsonplaceholder.typicode.com/posts/1/comments'
# URL = 'https://jsonplaceholder.typicode.com/comments?postId=1'
# URL = 'https://jsonplaceholder.typicode.com/posts?userId=1'

response = requests.get(URL)
data = response.json()

# print(data)
pprint(data)
