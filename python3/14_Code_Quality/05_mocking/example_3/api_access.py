from security import safe_requests


def api():
    response = safe_requests.get("https://www.google.com/", timeout=60)
    return response.status_code
