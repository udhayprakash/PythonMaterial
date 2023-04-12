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

    # Return a response
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "Function Name": function_name,
                "Function Version": function_version,
                "Log Group Name": log_group_name,
                "Log Stream Name": log_stream_name,
                "Memory Limit in MB": memory_limit_in_mb,
                "Invoked Function ARN": invoked_function_arn,
                "AWS Request ID": aws_request_id,
            }
        ),
    }
