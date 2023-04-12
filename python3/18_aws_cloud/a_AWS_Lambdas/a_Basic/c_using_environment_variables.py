"""
AWS Predefined Environment Variables
    AWS_LAMBDA_FUNCTION_NAME    - The name of the Lambda function.
    AWS_LAMBDA_FUNCTION_VERSION - The version number of the Lambda function.
    AWS_REGION                  - The AWS region in which the Lambda function is running.
    AWS_EXECUTION_ENV           - The runtime environment of the Lambda function.
    AWS_ACCESS_KEY_ID           - The access key ID used to invoke the Lambda function.
    AWS_SECRET_ACCESS_KEY       - The secret access key used to invoke the Lambda function.
    AWS_SESSION_TOKEN           - The session token used to invoke the Lambda function.
    AWS_DEFAULT_REGION          - The default AWS region to use for the SDK and CLI commands.
    AWS_ACCOUNT_ID              - The AWS account ID of the function's owner.
    AWS_COGNITO_IDENTITY        - The identity information for the Cognito user who invoked the Lambda function.
    AWS_LOG_GROUP_NAME          - The name of the CloudWatch Logs group where the logs are stored.
    AWS_LOG_STREAM_NAME         - The name of the CloudWatch Logs stream where the logs are stored.
    AWS_XRAY_DAEMON_ADDRESS     - The address of the X-Ray daemon.
    AWS_XRAY_CONTEXT_MISSING    - The behavior of the X-Ray SDK when it can't find a trace segment or subsegment.

"""
import json
import os


def lambda_handler(event, context):
    env_vars = {
        "NAME": os.environ.get("NAME", ""),
        "AGE": os.environ.get("AGE", ""),
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
