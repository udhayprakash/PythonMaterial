import json

import boto3


def lambda_handler(event, context):
    # Extract the bucket and key information from the event
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    # Use the boto3 client to access the S3 object
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=bucket, Key=key)
    content = obj["Body"].read().decode("utf-8")

    # Print the content of the S3 object
    print(f"Content of {key}:")
    print(content)

    # Return a response
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "S3 object processed successfully!"}),
    }

    return response
