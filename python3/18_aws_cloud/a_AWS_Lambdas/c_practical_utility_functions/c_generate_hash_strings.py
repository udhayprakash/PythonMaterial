import hashlib


def lambda_handler(event, context):
    text = event["text"]
    md5 = hashlib.md5(text.encode()).hexdigest()
    sha1 = hashlib.sha1(text.encode()).hexdigest()
    sha256 = hashlib.sha256(text.encode()).hexdigest()
    return {"statusCode": 200, "body": {"md5": md5, "sha1": sha1, "sha256": sha256}}


"""
eventData
    {
        'text': 'Hello World!'
    }
"""
