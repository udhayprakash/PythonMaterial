import json


def lambda_handler(event, context):
    # Extract metadata from the context object
    function_name = context.function_name
    function_version = context.function_version
    log_group_name = context.log_group_name
    log_stream_name = context.log_stream_name
    memory_limit_in_mb = context.memory_limit_in_mb
    invoked_function_arn = context.invoked_function_arn
    aws_request_id = context.aws_request_id

    # Print the extracted metadata
    print(f"Function Name: {function_name}")
    print(f"Function Version: {function_version}")
    print(f"Log Group Name: {log_group_name}")
    print(f"Log Stream Name: {log_stream_name}")
    print(f"Memory Limit in MB: {memory_limit_in_mb}")
    print(f"Invoked Function ARN: {invoked_function_arn}")
    print(f"AWS Request ID: {aws_request_id}")

    # Return a response
    return {"statusCode": 200, "body": json.dumps({"message": "Hello, world!"})}
