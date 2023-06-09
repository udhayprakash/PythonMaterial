import json

import requests

# r = requests.get('https://httpbin.org/stream/5', stream=True)

# # Method 1
# for line in r.iter_lines():
#     print()
#     # filter out keep-alive new lines
#     if line:
#         decoded_line = line.decode('utf-8')
#         print(json.loads(decoded_line))


# # Method 2
# print('\n\n\n')
# r = requests.get('https://httpbin.org/stream/5', stream=True)

# if r.encoding is None:
#     r.encoding = 'utf-8'

# for line in r.iter_lines(decode_unicode=True):
#     if line:
#         print(json.loads(line))


print("\n\n\n")
r = requests.get("https://httpbin.org/stream/5", stream=True)

if r.encoding is None:
    r.encoding = "utf-8"

for line in r.iter_content(decode_unicode=True, chunk_size=1024):
    if line:
        print(json.loads(line))
