#!/usr/bin/python
"""
Purpose:
"""
from openpyxl import Workbook


def create_workbook(path):
    workbook = Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Hello'
    sheet['A2'] = 213
    sheet['A3'] = 123.123
    sheet['B3'] = None
    sheet['B4'] = True
    sheet['B5'] = str((1, 2, 3))
    sheet['B6'] = str([1, 2, 3])
    sheet['C1'] = str({'a': 1})
    workbook.save(path)


if __name__ == '__main__':
    create_workbook('a_writing_excel.xlsx')
