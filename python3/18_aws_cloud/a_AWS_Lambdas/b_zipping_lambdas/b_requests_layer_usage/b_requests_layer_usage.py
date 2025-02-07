from security import safe_requests


def lambda_handler(event, context):
    response = safe_requests.get("https://www.google.com", timeout=60)
    return {"statusCode": 200, "body": response.content.decode()}


"""
pip install --platform manylinux2014_x86_64 --target=. --implementation cp --python 3.9 --only-binary=:all: --upgrade requests

"""
