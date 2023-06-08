import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

result = proxy.divide(10, 10)
print(f"{result =}")
print()

try:
    result = proxy.divide(10, 0)
except xmlrpc.client.Fault as error:
    print("Remote error:", error.faultString)
