import json


def lambda_handler(event, context):
    n = int(event["n"])
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return {"statusCode": 200, "result": json.dumps(fact)}


"""
event Data:
    {
        "n": 15
    }

"""
