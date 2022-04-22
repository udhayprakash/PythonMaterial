from pprint import pprint

import urllib3

print(f"{urllib3.__version__ =}")

"""
PoolManager
    - cache of connections that can be reused when needed in future requests
    - used to improve performance when executing commands numerous times
    - For reusing existing connections
"""
http = urllib3.PoolManager()

response = http.request("GET", "http://www.stackabuse.com")
print(response.status)  # Prints 200


http = urllib3.PoolManager(num_pools=3)

response1 = http.request("GET", "http://www.stackabuse.com")
response2 = http.request("GET", "http://www.google.com")


response = http.request("GET", "http://jsonplaceholder.typicode.com/posts/")
print(response.data.decode("utf-8"))
