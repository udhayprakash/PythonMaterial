import numpy as np


def lambda_handler(event, context):
    arr = np.array([[1, 2], [3, 4]])
    return {"statusCode": 200, "body": arr.tolist()}
