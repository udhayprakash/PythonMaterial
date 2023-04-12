import json


def lambda_handler(event, context):
    # Extract the query string parameters from the event
    params = event["queryStringParameters"]
    name = params["name"]
    age = params["age"]

    # Create a response object
    response_body = {"message": f"Hello, {name}! You are {age} years old."}

    # Return a response
    response = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response_body),
    }

    return response
