from gazpacho import get

url = "https://en.wikipedia.org/wiki/Gazpacho"
html = get(url)
print(html[:50], "\n\n")

# get, with optional params
url = "https://httpbin.org/anything"
html2 = get(
    url, params={"foo": "bar", "bar": "baz"}, headers={"User-Agent": "gazpacho"}
)
print(html2, "\n\n")
