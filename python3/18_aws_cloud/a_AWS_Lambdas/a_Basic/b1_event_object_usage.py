import json


def lambda_handler(event, context):
    # Extract values from the event object
    request_id = event["requestContext"]["requestId"]
    path = event["path"]
    http_method = event["httpMethod"]
    query_string_parameters = event["queryStringParameters"]
    headers = event["headers"]
    body = event["body"]

    # Print the extracted values
    print(f"Request ID: {request_id}")
    print(f"Path: {path}")
    print(f"HTTP Method: {http_method}")
    print(f"Query String Parameters: {query_string_parameters}")
    print(f"Headers: {headers}")
    print(f"Body: {body}")

    # Return a response
    return {"statusCode": 200, "body": json.dumps({"message": "Hello, world!"})}


{
    "requestContext": {"requestId": 1},
    "headers": "",
    "body": "",
    "path": "/tmp/path",
    "httpMethod": "GET",
    "queryStringParameters": {"pagenumber": 1, "pagesize": 10},
}
