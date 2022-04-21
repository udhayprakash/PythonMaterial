#!/usr/bin/python
"""
Purpose:
    https://currencylayer.com/quickstart
"""
from datetime import datetime

import requests

ACCESS_KEY = "96b5ca6a3116caa7a9b8985fd294243e"
API_URL = "http://www.apilayer.net/api/"


def get_live_currency_quote():
    URL = API_URL + "live?access_key=" + ACCESS_KEY
    response = requests.get(URL)
    # pprint(response.json())
    quotes = response.json().get("quotes")
    USDINR_quote = quotes.get("USDINR")
    # print(USDINR_quote)

    _timestamp = response.json().get("timestamp")
    timestamp = datetime.fromtimestamp(_timestamp)
    # print(timestamp)

    return """At {TIMESTAMP}, {QUOTE} is {QUOTE_VALUE}""".format(
        TIMESTAMP=timestamp, QUOTE="USDINR", QUOTE_VALUE=USDINR_quote
    )


def get_live_currency_quote2(requesting_data="live"):
    URL = API_URL + requesting_data
    request_params = {
        "access_key": ACCESS_KEY,
        "currencies": "USD,INR",  # ,AUD,CAD,PLN,MXN
        "format": 1
        # 'source': 'INR'
    }
    response = requests.get(URL, params=request_params).json()
    if response.get("error", {}):
        return response.get("error", {}).get("info")

    # pprint(response)
    quotes = response.get("quotes")
    USDINR_quote = quotes.get("USDINR")
    # print(USDINR_quote)

    _timestamp = response.get("timestamp")
    timestamp = datetime.fromtimestamp(_timestamp)
    # print(timestamp)

    return """At {TIMESTAMP}, {QUOTE} is {QUOTE_VALUE}""".format(
        TIMESTAMP=timestamp, QUOTE="USDINR", QUOTE_VALUE=USDINR_quote
    )


print(get_live_currency_quote())

print(get_live_currency_quote2())
# print(get_live_currency_quote2('historical'))
