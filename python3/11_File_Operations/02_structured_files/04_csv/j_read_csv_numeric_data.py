#!/usr/bin/python
"""
Purpose: Read numeric data from csv files

By default, data is read as a list of strings.
If we specify the QUOTE_NONNUMERIC format,
non-quoted values are converted into float values.

"""
import csv

with open('my_file.csv', dialect='excel') as fh:

    fh.close()
