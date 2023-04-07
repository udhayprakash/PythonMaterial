import io

from PIL import Image


def lambda_handler(event, context):
    with open("image.jpg", "rb") as f:
        img = Image.open(io.BytesIO(f.read()))
    img.save("/tmp/image.png")
    with open("/tmp/image.png", "rb") as f:
        image_data = f.read()
    return {
        "statusCode": 200,
        "body": image_data,
        "isBase64Encoded": True,
        "headers": {"Content-Type": "image/png"},
    }
