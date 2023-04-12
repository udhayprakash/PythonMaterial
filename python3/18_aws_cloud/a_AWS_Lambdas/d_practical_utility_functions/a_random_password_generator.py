import random
import string


def lambda_handler(event, context):
    length = int(event.get("password_length", 8))
    password = "".join(random.choices(string.ascii_letters + string.digits, k=length))
    return {"statusCode": 200, "body": password}


"""
eventData:
    {
        "password_length": 8
    }
"""
