import boto3

s3 = boto3.client("s3")


def lambda_handler(event, context):
    bucket_name = "example-bucket"
    file_name = "example-file.txt"
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        file_content = response["Body"].read().decode("utf-8")
        response = {"statusCode": 200, "body": file_content}
    except Exception as e:
        response = {"statusCode": 500, "body": str(e)}
    return response
