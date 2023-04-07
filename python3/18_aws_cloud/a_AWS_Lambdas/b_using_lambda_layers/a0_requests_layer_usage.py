import requests


def lambda_handler(event, context):
    response = requests.get("https://www.google.com")
    return {"statusCode": 200, "body": response.content.decode()}
