import requests
import json

url = 'http://localhost:5000'
payload = {
    "jsonrpc": "2.0",
    "method": "add",
    "params": [5, 3],
    "id": 1
}

response = requests.post(url, json=payload)
print(response.json())