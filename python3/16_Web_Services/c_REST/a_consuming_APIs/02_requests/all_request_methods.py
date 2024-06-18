import requests
from security import safe_requests

# Base URL for the HTTPBin API
base_url = "https://httpbin.org"

# Send a GET request to the /get endpoint
response = safe_requests.get(f"{base_url}/get", timeout=60)
print(response.json())

# Send a POST request to the /post endpoint with a JSON payload
payload = {"name": "Alice", "age": 30}
response = requests.post(f"{base_url}/post", json=payload, timeout=60)
print(response.json())

# Send a PUT request to the /put endpoint with a form data payload
payload = {"name": "Bob", "age": 40}
response = requests.put(f"{base_url}/put", data=payload, timeout=60)
print(response.json())

# Send a DELETE request to the /delete endpoint
response = requests.delete(f"{base_url}/delete", timeout=60)
print(response.json())

# Send a PATCH request to the /patch endpoint with a JSON payload
payload = {"name": "Charlie", "age": 50}
response = requests.patch(f"{base_url}/patch", json=payload, timeout=60)
print(response.json())

# Send a HEAD request to the /headers endpoint
response = requests.head(f"{base_url}/headers", timeout=60)
print(response.headers)

# Send a OPTIONS request to the /get endpoint
response = requests.options(f"{base_url}/get", timeout=60)
print(response.json())

# Send a GET request to the /status/{code} endpoint to simulate an error
response = safe_requests.get(f"{base_url}/status/404", timeout=60)
print(response.status_code)


# Send a GET request to the /stream/{n} endpoint to stream n lines of text
response = safe_requests.get(f"{base_url}/stream/5", stream=True, timeout=60)
for line in response.iter_lines():
    print(line.decode())

# Send a GET request to the /delay/{n} endpoint to simulate a delay of n seconds
response = safe_requests.get(f"{base_url}/delay/3", timeout=60)
print(response.json())

# Send a GET request to the /bytes/{n} endpoint to retrieve n bytes of random data
response = safe_requests.get(f"{base_url}/bytes/10", timeout=60)
print(response.content)

# Send a GET request to the /cookies endpoint to retrieve cookies set by the server
response = safe_requests.get(f"{base_url}/cookies", timeout=60)
print(response.cookies)

# Send a GET request to the /cookies/set endpoint to set a cookie
response = safe_requests.get(f"{base_url}/cookies/set", cookies={"name": "Alice"}, timeout=60)
print(response.cookies)

# Send a GET request to the /basic-auth/{user}/{passwd} endpoint to authenticate with HTTP basic authentication
response = safe_requests.get(f"{base_url}/basic-auth/user/passwd", auth=("user", "passwd"), timeout=60)
print(response.json())

# Send a GET request to the /bearer endpoint to authenticate with a bearer token
headers = {"Authorization": "Bearer mytoken"}
response = safe_requests.get(f"{base_url}/bearer", headers=headers, timeout=60)
print(response.json())

# Send a POST request to the /anything endpoint to receive and return any data
payload = {"name": "David", "age": 60}
response = requests.post(f"{base_url}/anything", json=payload, timeout=60)
print(response.json())

# Send a POST request to the /post endpoint with form data
payload = {"name": "Alice", "age": 30}
response = requests.post(f"{base_url}/post", data=payload, timeout=60)
print(response.json())

# Send a PUT request to the /put endpoint with binary data
payload = b"\x00\x01\x02\x03"
response = requests.put(f"{base_url}/put", data=payload, timeout=60)
print(response.content)

# Send a GET request to the /redirect/{n} endpoint to follow n redirects
response = safe_requests.get(f"{base_url}/redirect/3", timeout=60)
print(response.history)
print(response.url)

# Send a GET request to the /redirect-to endpoint to redirect to a URL
params = {"url": "https://www.google.com"}
response = safe_requests.get(f"{base_url}/redirect-to", params=params, timeout=60)
print(response.url)

# Send a POST request to the /post endpoint with a file upload
files = {"file": open("test.txt", "rb")}
response = requests.post(f"{base_url}/post", files=files, timeout=60)
print(response.json())

# Send a GET request to the /user-agent endpoint to retrieve the user agent string
response = safe_requests.get(f"{base_url}/user-agent", timeout=60)
print(response.json())

# Send a GET request to the /ip endpoint to retrieve the client's IP address
response = safe_requests.get(f"{base_url}/ip", timeout=60)
print(response.json())

# Send a GET request to the /headers endpoint with custom headers
headers = {"X-My-Header": "123"}
response = safe_requests.get(f"{base_url}/headers", headers=headers, timeout=60)
print(response.json())

# Send a GET request to the /hidden-basic-auth/{user}/{passwd} endpoint to authenticate with HTTP basic authentication
response = safe_requests.get(f"{base_url}/hidden-basic-auth/user/passwd", auth=("user", "passwd"), 
timeout=60)
print(response.json())

# Send a GET request to the /digest-auth/{qop}/{user}/{passwd}/{algorithm} endpoint to authenticate with digest authentication
response = safe_requests.get(f"{base_url}/digest-auth/auth/user/passwd/MD5", auth=("user", "passwd"), timeout=10
)
print(response.json())

# Send a GET request to the /bearer-auth/{token} endpoint to authenticate with a bearer token
headers = {"Authorization": "Bearer mytoken"}
response = safe_requests.get(f"{base_url}/bearer-auth/mytoken", headers=headers, timeout=60)
print(response.json())
