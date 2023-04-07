import csv


def lambda_handler(event, context):
    data = [["name", "age"], ["Alice", 30], ["Bob", 40], ["Charlie", 50]]
    csv_data = "\n".join([",".join(row) for row in data])
    return {
        "statusCode": 200,
        "body": csv_data,
        "headers": {"Content-Type": "text/csv"},
    }
