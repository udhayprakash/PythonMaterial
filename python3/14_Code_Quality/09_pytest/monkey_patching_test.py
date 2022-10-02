import requests


def get_number_fact(number):
    url = f"http://numbersapi.com/{number}?json"
    response = requests.get(url)
    json_resp = response.json()

    if json_resp["found"]:
        return json_resp["text"]

    return "No fact about this number."


# You don't want to call the API during your tests because:

# it's slow
# it's error-prone (the API can be down, you may have a poor internet connection, ...)


class MockedResponse:
    def __init__(self, json_body):
        self.json_body = json_body

    def json(self):
        return self.json_body


def mock_get(*args, **kwargs):
    return MockedResponse(
        {
            "text": "7 is the number of days in a week.",
            "found": "true",
        }
    )


def test_get_number_fact(monkeypatch):
    # Using pytest's builtin fixture to overwrite 'get' with mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    number = 7
    fact = "7 is the number of days in a week."

    assert get_number_fact(number) == fact


# ref - https://docs.pytest.org/en/7.1.x/how-to/monkeypatch.html
