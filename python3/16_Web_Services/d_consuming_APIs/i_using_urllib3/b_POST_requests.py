import urllib3

http = urllib3.PoolManager(4)


# Get with params

response = http.request(
    "GET", "http://jsonplaceholder.typicode.com/posts/", fields={"id": "1"}
)

print(response.data.decode("utf-8"))


# POST call
response = http.request(
    "POST",
    "http://jsonplaceholder.typicode.com/posts",
    fields={"title": "Created Post", "body": "Lorem ipsum", "userId": 5},
)
print(response.data.decode("utf-8"))


for i in range(1, 5):
    response = http.request(
        "DELETE", "http://jsonplaceholder.typicode.com/posts", fields={"id": i}
    )
    print(response.data.decode("utf-8"))


# PATCH request
data = {"title": "Updated title", "body": "Updated body"}

http = urllib3.PoolManager()

response = http.request("GET", "http://jsonplaceholder.typicode.com/posts/1")
print(response.data.decode("utf-8"))

response = http.request(
    "PATCH", "https://jsonplaceholder.typicode.com/posts/1", fields=data
)
print(response.data.decode("utf-8"))


# URL: https://official-joke-api.appspot.com/jokes/programming/random

# Validate that the returned Joke is of type "programming" in case only one joke is expected
# Validate that the returned Joke is of type "programming" in case more than one joke is expected ( will work with one joke returned, as well)

# URL_10: https://official-joke-api.appspot.com/jokes/programming/ten

# Validate that 10 jokes are returned
# Validate that all jokes are of type "programming"


from urllib import request

req = request.Request("https://postman-echo.com/post", method="POST")
r = request.urlopen(req)
content = r.read()
print(content)

import json
from urllib import request

req = request.Request("https://postman-echo.com/post", method="POST")
req.add_header("Content-Type", "application/json")
data = {"hello": "world"}
data = json.dumps(data)
data = data.encode()
r = request.urlopen(req, data=data)
content = r.read()
print(content)
