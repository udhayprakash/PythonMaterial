import xlsxwriter
from datetime import datetime
from pytz import utc

# default date format
workbook = xlsxwriter.Workbook('datetimes.xlsx', {
    'default_date_format':'dd/mm/yy',
    # 'remove_timezone': True
    })

worksheet = workbook.add_worksheet()

date_time = datetime.now()
worksheet.write_datetime(0, 0, date_time)  # Formatted as 'dd/mm/yy'


# Timezone handling
utc_datetime = datetime(2016, 9, 23, 14, 13, 21, tzinfo=utc)
naive_datetime = utc_datetime.replace(tzinfo=None)

worksheet.write_datetime(1, 0, naive_datetime)

workbook.close()
