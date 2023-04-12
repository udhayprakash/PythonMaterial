import boto3

s3 = boto3.resource("s3")


def lambda_handler(event, context):
    bucket_name = "example-bucket"
    try:
        s3.create_bucket(Bucket=bucket_name)
        response = {
            "statusCode": 200,
            "body": f"S3 bucket {bucket_name} created successfully",
        }
    except Exception as e:
        response = {"statusCode": 500, "body": str(e)}
    return response
