#!/usr/bin/python3
"""
Purpose: To display the progress as below:
 32% (16 of 50) |################### 
    pip install -U progressbar --user
"""
from time import sleep
from progressbar import ProgressBar

bar = ProgressBar()
for i in bar(range(50)):
    sleep(0.5)
