def lambda_handler(event, context):
    html = "<html><body><h1>Hello, world!</h1></body></html>"
    return {"statusCode": 200, "body": html, "headers": {"Content-Type": "text/html"}}
