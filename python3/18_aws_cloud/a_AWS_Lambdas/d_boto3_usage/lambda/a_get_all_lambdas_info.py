import boto3


def lambda_handler(event, context):
    client = boto3.client("lambda")
    response = client.list_functions()
    functions = response["Functions"]

    function_metadata = []
    for function in functions:
        metadata = {}
        metadata["FunctionName"] = function["FunctionName"]
        metadata["Description"] = function["Description"]
        metadata["Runtime"] = function["Runtime"]
        metadata["LastModified"] = function["LastModified"].strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        metadata["CodeSize"] = function["CodeSize"]
        metadata["MemorySize"] = function["MemorySize"]
        metadata["Timeout"] = function["Timeout"]
        metadata["Role"] = function["Role"]
        function_metadata.append(metadata)

    return {
        "statusCode": 200,
        "body": function_metadata,
        "headers": {"Content-Type": "application/json"},
    }
