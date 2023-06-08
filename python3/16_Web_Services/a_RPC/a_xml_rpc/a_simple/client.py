import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
response = proxy.hello()

print(f"{response =}")
