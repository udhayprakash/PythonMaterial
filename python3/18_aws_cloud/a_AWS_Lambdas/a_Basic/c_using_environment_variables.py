import json
import os


def lambda_handler(event, context):
    env_vars = {
        "AWS_REGION": os.environ.get("AWS_REGION"),
        "AWS_EXECUTION_ENV": os.environ.get("AWS_EXECUTION_ENV"),
        "AWS_LAMBDA_FUNCTION_NAME": os.environ.get("AWS_LAMBDA_FUNCTION_NAME"),
        "AWS_LAMBDA_FUNCTION_VERSION": os.environ.get("AWS_LAMBDA_FUNCTION_VERSION"),
        "AWS_LAMBDA_LOG_GROUP_NAME": os.environ.get("AWS_LAMBDA_LOG_GROUP_NAME"),
        "AWS_LAMBDA_LOG_STREAM_NAME": os.environ.get("AWS_LAMBDA_LOG_STREAM_NAME"),
        "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID"),
        "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY"),
        "AWS_SESSION_TOKEN": os.environ.get("AWS_SESSION_TOKEN"),
        "AWS_S3_BUCKET_NAME": os.environ.get("AWS_S3_BUCKET_NAME"),
        "AWS_SQS_QUEUE_NAME": os.environ.get("AWS_SQS_QUEUE_NAME"),
        "AWS_DYNAMODB_TABLE_NAME": os.environ.get("AWS_DYNAMODB_TABLE_NAME"),
        "AWS_RDS_HOSTNAME": os.environ.get("AWS_RDS_HOSTNAME"),
        "AWS_RDS_PORT": os.environ.get("AWS_RDS_PORT"),
        "AWS_RDS_DB_NAME": os.environ.get("AWS_RDS_DB_NAME"),
        "AWS_RDS_USERNAME": os.environ.get("AWS_RDS_USERNAME"),
        "AWS_RDS_PASSWORD": os.environ.get("AWS_RDS_PASSWORD"),
    }

    return {"statusCode": 200, "body": json.dumps(env_vars)}
