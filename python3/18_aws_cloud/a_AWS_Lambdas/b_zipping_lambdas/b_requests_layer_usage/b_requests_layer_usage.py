import requests


def lambda_handler(event, context):
    response = requests.get("https://www.google.com")
    return {"statusCode": 200, "body": response.content.decode()}


"""
pip install --platform manylinux2014_x86_64 --target=. --implementation cp --python 3.9 --only-binary=:all: --upgrade requests

"""
