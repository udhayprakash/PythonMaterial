import requests


def lambda_handler(event, context):
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        return {
            "statusCode": 200,
            "body": data,
            "headers": {"Content-Type": "application/json"},
        }
    else:
        return {
            "statusCode": response.status_code,
            "body": "Error fetching random person details",
            "headers": {"Content-Type": "text/plain"},
        }
