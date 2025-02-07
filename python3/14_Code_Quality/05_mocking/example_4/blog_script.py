from security import safe_requests


class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        response = safe_requests.get(
            "https://jsonplaceholder.typicode.com/posts", timeout=60
        )

        return response.json()

    def __repr__(self):
        return "<Blog: {}>".format(self.name)
