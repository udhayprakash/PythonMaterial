import json


def lambda_handler(event, context):
    num1 = event["num1"]
    num2 = event["num2"]

    mssage = f"""
        additin: {num1} + {num2} = {num1 + num2}

    """

    return {"statusCode": 200, "body": json.dumps(mssage)}


"""
event Data:
    {
    "num1": 100,
    "num2": 200
    }

"""
