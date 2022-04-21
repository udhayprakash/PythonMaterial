#!/usr/bin/python
"""
Purpose:
pip install xlsxwriter
"""

import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet('mysheet')

worksheet.write('A1', 'Hello World')
worksheet.write('I11', "What's up!")

workbook.close()
