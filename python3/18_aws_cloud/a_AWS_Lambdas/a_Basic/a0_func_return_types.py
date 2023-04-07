import json


def lambda_handler(event, context):
    # # return string
    # return 'Hello, world!'

    # # return int
    # return 42

    # # return list
    # return ['Hello', 'world!']

    # return dict
    data = {"name": "Alice", "age": 30}
    return {"statusCode": 200, "body": json.dumps(data)}
