#!/usr/bin/python
"""
purpose: regular expression  demo 

To get alll CRITICAL level log lines in log file
"""

import re
import datetime

today_date = datetime.datetime.now().strftime('%d-%b-%Y')

with open('logging_ex_5.log', 'r') as fh:
    log_file_content = fh.read()

    # print(log_file_content)
    print()
    critical_log_lines = re.findall(today_date + '.*- CRITICAL -.*', log_file_content)

    for each_line in critical_log_lines:
        print(each_line)

    fh.close()
