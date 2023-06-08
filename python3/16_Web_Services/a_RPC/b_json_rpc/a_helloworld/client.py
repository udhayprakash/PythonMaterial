import jsonrpcclient

response = jsonrpcclient.request("http://localhost:8000", "hello")
print(response.text)
