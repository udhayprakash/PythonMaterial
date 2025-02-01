import requests
import json

url = 'http://localhost:5001'
payload = {
    "jsonrpc": "2.0",
    "method": "concatenate",
    "params": ["Hello, ", "World!"],
    "id": 1
}

response = requests.post(url, json=payload)
print(response.json())