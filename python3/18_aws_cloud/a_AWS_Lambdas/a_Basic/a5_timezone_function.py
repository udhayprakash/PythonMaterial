from datetime import datetime, timedelta, timezone


def lambda_handler(event, context):
    tz = event["timezone"]
    #     return {
    #         'statusCode': 200,
    #         'body': json.dumps('Hello from Lambda!')
    #     }

    return str(datetime.now(timezone(timedelta(hours=tz))))


"""
event Data:
    {
    "timezone": 5.5
    }

"""
