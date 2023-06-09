from pprint import pp

import requests

# Exercise 1.1
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response status code equals 200
response = requests.get("http://api.zippopotam.us/us/90210")
print(response)
print(f"{response.status_code =}")

# Exercise 1.2
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the value of the response header 'Content-Type' equals 'application/json'
resp_headers = dict(response.headers)
pp(resp_headers)
print(resp_headers["Content-Type"])

# Exercise 1.3
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body encoding is not set (equal to None)
print(response.content)
print(response.text)
pp(response.json())

# Exercise 1.4
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body element 'country' has a value equal to 'United States'
response_data = response.json()
print(response_data["country"] == "United States")

# Exercise 1.5
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the first 'place name' element in the list of places
# has a value equal to 'Beverly Hills'
print()
print([each["place name"] for each in response_data["places"]])

# Exercise 1.6
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body element 'places' has an array
# value with a length of 1 (i.e., there's one place that corresponds
# to the US zip code 90210)
assert len(response_data["places"]) == 1
