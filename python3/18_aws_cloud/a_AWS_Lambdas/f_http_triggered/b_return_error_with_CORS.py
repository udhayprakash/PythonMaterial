def lambda_handler(event, context):
    return {
        "statusCode": 400,
        "headers": {
            "Content-Type": "text/plain",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": "Invalid input",
    }
