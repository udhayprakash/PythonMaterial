import base64


def lambda_handler(event, context):
    with open("/tmp/image.jpg", "wb") as f:
        f.write(base64.b64decode(event["body"]))

    with open("/tmp/image.jpg", "rb") as f:
        image_data = f.read()

    encoded_data = base64.b64encode(image_data).decode("utf-8")

    return {
        "statusCode": 200,
        "body": encoded_data,
        "isBase64Encoded": True,
        "headers": {"Content-Type": "image/jpeg"},
    }
