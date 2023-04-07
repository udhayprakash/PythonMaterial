from PIL import Image


def lambda_handler(event, context):
    img = Image.new("RGB", (200, 200), color="red")
    img.save("/tmp/red.png")
    return {"statusCode": 200, "body": "Image saved as /tmp/red.png"}
