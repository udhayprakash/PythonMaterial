def lambda_handler(event, context):
    return {
        "statusCode": 400,
        "body": "Bad request",
        "headers": {"Content-Type": "text/plain"},
    }
