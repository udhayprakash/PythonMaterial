import requests

DUCKDUCKGO_URL = 'https://api.duckduckgo.com/?q={query_string}&format=json&pretty=1'

search_string = raw_input('Enter the content to search:\n')
response = requests.get(DUCKDUCKGO_URL.format(query_string=search_string))
if response.status_code == 200:
    # print response.text
    with open('result.json', 'wb') as f:
        f.write(response.text)
        f.close()
