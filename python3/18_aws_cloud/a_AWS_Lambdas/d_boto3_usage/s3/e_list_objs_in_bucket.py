import boto3

s3 = boto3.client("s3")


def lambda_handler(event, context):
    bucket_name = "example-bucket"
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        object_list = [obj["Key"] for obj in response["Contents"]]
        response = {"statusCode": 200, "body": object_list}
    except Exception as e:
        response = {"statusCode": 500, "body": str(e)}
    return response
