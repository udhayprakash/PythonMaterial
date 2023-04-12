import base64
import io

import qrcode


def lambda_handler(event, context):
    url = event["url"]
    img = qrcode.make(url)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    return {
        "statusCode": 200,
        "body": base64.b64encode(img_bytes.getvalue()).decode("utf-8"),
        "isBase64Encoded": True,
        "headers": {"Content-Type": "image/png"},
    }


"""
eventData:
{
    "url": "https://www.example.com"
}
"""
