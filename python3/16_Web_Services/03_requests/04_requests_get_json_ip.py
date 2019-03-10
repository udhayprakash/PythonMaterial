import requests
 
r = requests.get('http://httpbin.org/ip')
print(r.headers['content-type'])
if r.status_code == 200:
    print(r.text)
    data = r.json()
    print(data)
    print(data['origin'])
else:
    print r.status_code
