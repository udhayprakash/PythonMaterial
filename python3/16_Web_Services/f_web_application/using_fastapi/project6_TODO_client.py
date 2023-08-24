import requests

URL = "http://localhost:8000"

# Create item
item = {"id": 1, "name": "Foo", "price": 29.99}
response = requests.post(f"{URL}/items", json=item)

# Get item
response = requests.get(f"{URL}/items/1")

# Update item
updated_item = {"id": 1, "name": "Bar", "price": 39.99}
response = requests.put(f"{URL}/items/1", json=updated_item)

# Delete item
response = requests.delete(f"{URL}/items/1")
