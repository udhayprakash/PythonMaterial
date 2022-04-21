#!/usr/bin/python
"""
Purpose: working with timezone
pip install pytz
"""

import pytz
import datetime

kiev_tz = pytz.timezone('Europe/Kiev')
kiev_tz.zone

dt = kiev_tz.localize(datetime.datetime(2014, 11, 2, 15, 25, 0))

fmt = '%Y-%m-%d %H:%M:%S %Z%z'
dt.strftime(fmt)

utc_dt = datetime.datetime(2014, 11, 2, 15, 25, 0, tzinfo=pytz.utc)
dt = utc_dt.astimezone(kiev_tz)
dt.strftime(fmt)

now = datetime.datetime.utcnow().replace(tzinfo = pytz.utc)
now.astimezone(kiev_tz)
