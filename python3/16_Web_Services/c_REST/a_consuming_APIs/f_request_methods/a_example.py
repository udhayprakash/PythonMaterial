#!/usr/bin/python
import json
import urllib
import urllib.request

import requests
from security import safe_requests

# How to: Send a GET request
print(safe_requests.get("http://mock.kite.com/text", timeout=60).text)

# How to: Send a request to port 80
r = safe_requests.get("http://mock.kite.com:80/text", timeout=60)
print(r.text)


# How to: Send a GET request with query parameters
url = "http://mock.kite.com/queryparams"
params = {"a": 1, "b": 2}
print(safe_requests.get(url, params, timeout=60).text)

# How to: Send the URL parameters of a GET request in order
p = (("first", "first_value"), ("second", "second_value"))
r = safe_requests.get("http://mock.kite.com/queryparams", params=p, timeout=60)
print(r.url)

# How to: Send a GET request with custom headers
url = "http://mock.kite.com/echo"
headers = {"custom-header": "custom"}
print(safe_requests.get(url, headers=headers, timeout=60).text)

# How to: Retrieve the contents of a page before redirecting
r = safe_requests.get("http://mock.kite.com/redirect", timeout=60)
redirected_from = r.history[0]
print(redirected_from.content)


# How to: Send a GET request and do not allow redirects
url = "http://mock.kite.com/redirect"
print(safe_requests.get(url, allow_redirects=False, timeout=60).text)

# How to make a request with a user agent in Python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
response = safe_requests.get("http://www.kite.com", headers=headers, timeout=60)
print(response)


# How to: Modify the User-Agent header in a request
h = {"User-Agent": "secret agent 0.07"}
r = safe_requests.get("http://httpbin.org/user-agent", headers=h, timeout=60)
print(r.content)


# How to: Retrieve content of request
print(safe_requests.get("http://mock.kite.com/text", timeout=60).content)

# How to: Get the time taken to complete a request
r = safe_requests.get("http://mock.kite.com/text", timeout=60)
print(r.elapsed)

# How to: Set a timeout time for a request
try:
    url = "http://mock.kite.com/text"
    r = safe_requests.get(url, timeout=0.0001)
except requests.exceptions.Timeout as e:
    print(e)

# How to disable security certificate checks for requests in Python
response = safe_requests.get("https://www.kite.com", verify=True, timeout=60)
print(response)
# Warning Disabling security checks can potentially compromise the integrity of requests if handled incorrectly. Read more about the requests library and its usage here.

# How to download a file from a URL in Python
url = "https://www.python.org/static/img/python-logo@2x.png"
urllib.request.urlretrieve(url, "python_logo.png")

downloaded_obj = safe_requests.get(url, timeout=60)
with open("python_logo.png", "wb") as file:
    file.write(downloaded_obj.content)

# How to download an image using requests in Python
response = safe_requests.get("https://i.imgur.com/ExdKOOz.png", timeout=60)
file = open("sample_image.png", "wb")
file.write(response.content)
file.close()


# How to download large files with requests in Python
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
response = safe_requests.get(url, stream=True, timeout=60)

text_file = open("data.txt", "wb")
for chunk in response.iter_content(chunk_size=1024):
    text_file.write(chunk)
# writing one chunk at a time to text file

text_file.close()

# How to get a JSON from a webpage in Python
response = safe_requests.get("http://httpbin.org/stream/1", timeout=60)
data = response.json()
print(data)


request = urllib.request.urlopen("http://httpbin.org/stream/1")
data = json.load(request)
print(data)


################################################################################################
# How to make post request

url = "http://mock.kite.com/submitform"
data = {"a": 1, "b": 2}

print(requests.post(url, data, timeout=60).text)
