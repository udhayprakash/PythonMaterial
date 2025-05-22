import requests
from security import safe_requests

URL = "http://localhost:8000"

# Create item
item = {"id": 1, "name": "Foo", "price": 29.99}
response = requests.post(f"{URL}/items", json=item, timeout=60)

# Get item
response = safe_requests.get(f"{URL}/items/1", timeout=60)

# Update item
updated_item = {"id": 1, "name": "Bar", "price": 39.99}
response = requests.put(f"{URL}/items/1", json=updated_item, timeout=60)

# Delete item
response = requests.delete(f"{URL}/items/1", timeout=60)
