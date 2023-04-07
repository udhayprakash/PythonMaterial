import json


def lambda_handler(event, context):
    # 1: Get the current time from the context object
    current_time = context.get_remaining_time_in_millis()

    # 2: Get the AWS request ID from the context object
    aws_request_id = context.aws_request_id

    # 3: Get the function name from the context object
    function_name = context.function_name

    # 4: Get the function version from the context object
    function_version = context.function_version

    # 5: Get the log group name from the context object
    log_group_name = context.log_group_name

    # 6: Get the log stream name from the context object
    log_stream_name = context.log_stream_name

    # 7: Get the memory limit from the context object
    memory_limit = context.memory_limit_in_mb

    # 8: Get the invoked function ARN from the context object
    invoked_function_arn = context.invoked_function_arn

    # 9: Get the remaining time in seconds from the context object
    remaining_time_in_seconds = context.get_remaining_time_in_millis() / 1000

    # 10: Get the client context from the context object
    client_context = context.client_context

    # 11: Get the function execution ID from the context object
    function_execution_id = context.aws_request_id.split("-")[1]

    # 12: Get the function memory usage from the context object
    function_memory_usage = context.memory_limit_in_mb - context.memory_left

    # 13: Get the function duration from the context object
    function_duration = context.get_remaining_time_in_millis()

    # 14: Get the function start time from the context object
    function_start_time = context.get_remaining_time_in_millis()

    # 15: Get the function end time from the context object
    function_end_time = context.get_remaining_time_in_millis()

    # 16: Get the function cold start status from the context object
    function_cold_start = (
        context.function_name == context.invoked_function_arn.split(":")[-1]
    )

    # 17: Get the function request ID from the event object
    request_id = event["request_id"]

    # 18: Get the function user ID from the event object
    user_id = event["user_id"]

    # 19: Get the function action type from the event object
    action_type = event["action_type"]

    # 20: Get the function action value from the event object
    action_value = event["action_value"]

    # Combine all results into a single dictionary
    return {
        "current_time": current_time,
        "aws_request_id": aws_request_id,
        "function_name": function_name,
        "function_version": function_version,
        "log_group_name": log_group_name,
        "log_stream_name": log_stream_name,
        "memory_limit": memory_limit,
        "invoked_function_arn": invoked_function_arn,
        "remaining_time_in_seconds": remaining_time_in_seconds,
        "client_context": client_context,
        "function_execution_id": function_execution_id,
        "function_memory_usage": function_memory_usage,
        "function_duration": function_duration,
        "function_start_time": function_start_time,
        "function_end_time": function_end_time,
        "function_cold_start": function_cold_start,
        "request_id": request_id,
        "user_id": user_id,
        "action_type": action_type,
        "action_value": action_value,
        "event": event,
        "context": context,
    }
