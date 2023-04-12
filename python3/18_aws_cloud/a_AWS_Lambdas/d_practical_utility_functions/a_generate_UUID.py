import uuid


def lambda_handler(event, context):
    uuid_string = str(uuid.uuid4())
    return {"statusCode": 200, "body": uuid_string}
