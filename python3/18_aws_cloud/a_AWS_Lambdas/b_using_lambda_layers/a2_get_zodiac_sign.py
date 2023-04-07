import json

import requests


def lambda_handler(event, context):
    dob = event["dob"]  # format yyyy-mm-dd
    month, day, year = dob.split("-")
    url = f"https://aztro.sameerkumar.website/?day={day}&month={month}&year={year}&timezone=Asia/Kolkata"
    response = requests.post(url)
    data = json.loads(response.text)
    sign = data["sign"]
    return {"statusCode": 200, "body": f"Your zodiac sign is {sign}"}


"""
eventData:
{
    "dob": "1990-01-01"
}
"""
