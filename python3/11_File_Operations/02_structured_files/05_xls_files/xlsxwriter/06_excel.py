#!/usr/bin/python
"""
Purpose:
--------------------------------------------------------------
(0, 0)      # Row-column notation.
('A1')      # The same cell in A1 notation.

(6, 2)      # Row-column notation.
('C7')      # The same cell in A1 notation.
--------------------------------------------------------------
Relative cell references change when they are copied while
Absolute references maintain fixed row and/or column references.
'A1'    # Column and row are relative.
'$A1'   # Column is absolute and row is relative.
'A$1'   # Column is relative and row is absolute.
'$A$1'  # Column and row are absolute.
"""
import xlsxwriter

with xlsxwriter.Workbook('mybook.xlsx') as wb:
    ws = wb.add_worksheet()

    for row in range(0, 5):
        ws.write(row, 0, 'Hello')

    ws.write('D1', 200)
    ws.write('D2', '=H1+1')

    data = {
        'first_name': 'Bharath',
        'last_name': 'India',
        'age': 70,
        'currency': 'INR',
        'capital': 'New Delhi'
    }

    ws2 = wb.add_worksheet('Countries')
    # row = 0
    col = 0
    ws2.write_row(row, col, tuple(data.keys()))
    row += 1
    ws2.write_row(row, col, tuple(data.values()))

    # ws.write('B2', 150)
    # wb.define_name('Exchange_rate', '=0.96')
    # ws.write('B3', '=B2*Exchange_rate')
