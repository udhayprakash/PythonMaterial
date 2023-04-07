import json


def lambda_handler(event, context):
    person_name = event.get("name", "no such key")
    return {"statusCode": 200, "body": json.dumps(f"Hello from  {person_name}!")}


"""
event Data:
    {
    "name": "udhay",
    }

"""
