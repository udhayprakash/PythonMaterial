import urllib.parse


def lambda_handler(event, context):
    url = event["url"]
    encoded_url = urllib.parse.quote(url)
    decoded_url = urllib.parse.unquote(encoded_url)
    return {"statusCode": 200, "body": decoded_url}


"""
event Data:
    {
        'url': 'https://www.example.com/search?q=python lambda'
    }
"""
