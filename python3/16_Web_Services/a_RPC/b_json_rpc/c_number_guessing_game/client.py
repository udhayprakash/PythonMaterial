import requests
import json

url = 'http://localhost:5000'

while True:
    guess = int(input("Enter your guess (1-100): "))
    payload = {
        "jsonrpc": "2.0",
        "method": "guess",
        "params": [guess],
        "id": 1
    }

    response = requests.post(url, json=payload)
    result = response.json()

    print(result['result'])

    if "Correct!" in result['result']:
        break
