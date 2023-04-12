import pandas as pd


def lambda_handler(event, context):
    data = {"name": ["John", "Jane", "Bob"], "age": [25, 30, 35]}
    df = pd.DataFrame(data)
    return {"statusCode": 200, "body": df.to_json()}
