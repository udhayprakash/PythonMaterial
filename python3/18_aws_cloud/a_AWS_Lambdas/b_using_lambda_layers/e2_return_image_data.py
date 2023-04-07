import base64

from PIL import Image


def lambda_handler(event, context):
    img = Image.new("RGB", (200, 200), color="red")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode("ascii")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "image/png"},
        "body": img_str,
        "isBase64Encoded": True,
    }
