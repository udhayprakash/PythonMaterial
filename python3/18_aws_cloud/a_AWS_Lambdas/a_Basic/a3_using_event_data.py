import json


def lambda_handler(event, context):
    name = event["name"]

    # Construct the response JSON
    response = {"message": f"Hello {name}!"}

    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }

    # Return the response JSON
    return {
        "statusCode": 200,
        "body": json.dumps(response),
        "headers": {"Content-Type": "application/json"},
    }


"""
event Data:
    {
    "name": "udhay",
    }

"""
