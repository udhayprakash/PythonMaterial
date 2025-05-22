from security import safe_requests

DUCKDUCKGO_URL = "https://api.duckduckgo.com/?q={query_string}&format=json&pretty=1"

search_string = input("Enter the content to search:\n")
response = safe_requests.get(DUCKDUCKGO_URL.format(query_string=search_string), timeout=60)
if response.status_code == 200:
    # print(response.text)
    with open("result.json", "wb") as f:
        f.write(response.text)
        f.close()
