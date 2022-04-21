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
