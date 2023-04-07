def lambda_handler(event, context):
    return {"statusCode": 302, "headers": {"Location": "https://example.com"}}
