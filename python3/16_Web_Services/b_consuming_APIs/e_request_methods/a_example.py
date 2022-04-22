#!/usr/bin/python
import json
import urllib
import urllib.request

import requests

# How to: Send a GET request
print(requests.get("http://mock.kite.com/text").text)

# How to: Send a request to port 80
r = requests.get("http://mock.kite.com:80/text")
print(r.text)


# How to: Send a GET request with query parameters
url = "http://mock.kite.com/queryparams"
params = {"a": 1, "b": 2}
print(requests.get(url, params).text)

# How to: Send the URL parameters of a GET request in order
p = (("first", "first_value"), ("second", "second_value"))
r = requests.get("http://mock.kite.com/queryparams", params=p)
print(r.url)

# How to: Send a GET request with custom headers
url = "http://mock.kite.com/echo"
headers = {"custom-header": "custom"}
print(requests.get(url, headers=headers).text)

# How to: Retrieve the contents of a page before redirecting
r = requests.get("http://mock.kite.com/redirect")
redirected_from = r.history[0]
print(redirected_from.content)


# How to: Send a GET request and do not allow redirects
url = "http://mock.kite.com/redirect"
print(requests.get(url, allow_redirects=False).text)

# How to make a request with a user agent in Python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
response = requests.get("http://www.kite.com", headers=headers)
print(response)


# How to: Modify the User-Agent header in a request
h = {"User-Agent": "secret agent 0.07"}
r = requests.get("http://httpbin.org/user-agent", headers=h)
print(r.content)


# How to: Retrieve content of request
print(requests.get("http://mock.kite.com/text").content)

# How to: Get the time taken to complete a request
r = requests.get("http://mock.kite.com/text")
print(r.elapsed)

# How to: Set a timeout time for a request
try:
    url = "http://mock.kite.com/text"
    r = requests.get(url, timeout=0.0001)
except requests.exceptions.Timeout as e:
    print(e)

# How to disable security certificate checks for requests in Python
response = requests.get("https://www.kite.com", verify=False)
print(response)
# Warning Disabling security checks can potentially compromise the integrity of requests if handled incorrectly. Read more about the requests library and its usage here.

# How to download a file from a URL in Python
url = "https://www.python.org/static/img/python-logo@2x.png"
urllib.request.urlretrieve(url, "python_logo.png")

downloaded_obj = requests.get(url)
with open("python_logo.png", "wb") as file:
    file.write(downloaded_obj.content)

# How to download an image using requests in Python
response = requests.get("https://i.imgur.com/ExdKOOz.png")
file = open("sample_image.png", "wb")
file.write(response.content)
file.close()


# How to download large files with requests in Python
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
response = requests.get(url, stream=True)

text_file = open("data.txt", "wb")
for chunk in response.iter_content(chunk_size=1024):
    text_file.write(chunk)
# writing one chunk at a time to text file

text_file.close()

# How to get a JSON from a webpage in Python
response = requests.get("http://httpbin.org/stream/1")
data = response.json()
print(data)


request = urllib.request.urlopen("http://httpbin.org/stream/1")
data = json.load(request)
print(data)


################################################################################################
# How to make post request

url = "http://mock.kite.com/submitform"
data = {"a": 1, "b": 2}

print(requests.post(url, data).text)
