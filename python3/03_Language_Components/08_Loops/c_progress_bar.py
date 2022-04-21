#!/usr/bin/python3
"""
Purpose: To display the progress as below:
 32% (16 of 50) |###################

 pip install --upgrade progressbar --user
"""
import time
import progressbar

bar = progressbar.ProgressBar()
print(bar)

for i in bar(range(50)):
    time.sleep(2)  # seconds
