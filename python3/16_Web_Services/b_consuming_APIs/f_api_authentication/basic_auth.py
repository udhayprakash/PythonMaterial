import sys

import requests


def login(_username, _password):
    url = "http://httpbin.org/basic-auth/user/passwd"

    response = requests.get(url, auth=(_username, _password))
    if response.status_code != 200:
        print("Error found", response.status_code, file=sys.stderr)
        print(response.reason)
        return response.reason

    response_data = response.json()
    if response_data["authenticated"]:
        print("Authentication Successful")


if __name__ == "__main__":
    login("user", "passwd")
    login("user", "passwd123")
