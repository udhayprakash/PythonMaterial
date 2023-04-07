from datetime import datetime

import pytz


def lambda_handler(event, context):
    timezones = pytz.all_timezones
    current_time = datetime.now()
    results = {}
    for tz in timezones:
        timezone = pytz.timezone(tz)
        results[tz] = current_time.astimezone(timezone).strftime("%Y-%m-%d %H:%M:%S")
    return {"statusCode": 200, "body": results}
