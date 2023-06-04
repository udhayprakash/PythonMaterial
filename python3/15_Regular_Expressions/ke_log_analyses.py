"""
Purpose: Log Analyses using regular expressions

To get all CRITICAL level log lines in log file
"""

import os
import re

os.chdir("../11_Logging")
print(os.getcwd())

# Method 1 - traditional
with open("07_file_handler.log", "r") as f:
    file_content = f.readlines()
    critical_logs = []
    for each_line in file_content:
        if "CRITICAL" in each_line:
            critical_logs.append(each_line)
    f.close()

print(critical_logs)

# Method 2 - using re
with open("07_file_handler.log", "r") as f:
    file_content = f.read()
    critical_logs = re.findall(".*CRITICAL.*", file_content)
    f.close()

critical_event_times = []
for each_log in critical_logs:
    # print(each_log)
    log_time = re.match(r"\d+-\d+-\d+\s\d+:\d+:\d+,\d+", each_log).group()
    critical_event_times.append(critical_event_times)

print(critical_event_times)
