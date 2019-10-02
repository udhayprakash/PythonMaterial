import datetime as dt
import pytz

naive_utc_now = dt.datetime.utcnow()
print('naive utc now: {}     , tzinfo: {}'.format(
    naive_utc_now, naive_utc_now.tzinfo))

# Localizing naive datetimes
UTC_TZ = pytz.timezone('UTC')
utc_now = UTC_TZ.localize(naive_utc_now)
print('utc now      : {}, tzinfo: {}'.format(utc_now, utc_now.tzinfo))

# Converting localized datetimes to different timezone
PARIS_TZ = pytz.timezone('Europe/Paris')
paris_now = PARIS_TZ.normalize(utc_now)
print('Paris        : {}, tzinfo: {}'.format(paris_now, paris_now.tzinfo))

NEW_YORK_TZ = pytz.timezone('America/New_York')
ny_now = NEW_YORK_TZ.normalize(utc_now)
print('New York     : {}, tzinfo: {}'.format(ny_now, ny_now.tzinfo))

IST_TZ = pytz.timezone('India/Kolkatta')
ist_now = IST_TZ.normalize(utc_now)
print('New York     : {}, tzinfo: {}'.format(ist_now, ist_now.tzinfo))
