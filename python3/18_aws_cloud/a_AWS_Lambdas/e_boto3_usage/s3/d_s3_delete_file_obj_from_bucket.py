import boto3

s3 = boto3.client("s3")


def lambda_handler(event, context):
    bucket_name = "example-bucket"
    file_name = "example-file.txt"
    try:
        s3.delete_object(Bucket=bucket_name, Key=file_name)
        response = {
            "statusCode": 200,
            "body": f"File {file_name} deleted from S3 bucket {bucket_name} successfully",
        }
    except Exception as e:
        response = {"statusCode": 500, "body": str(e)}
    return response
