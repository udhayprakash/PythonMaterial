import requests
from pprint import pprint

r = requests.get('http://httpbin.org/user-agent')

pprint(r.headers)

print(r.headers['content-type'])
print(r.text)
data = r.json()
print(data)
print(data['user-agent'])
