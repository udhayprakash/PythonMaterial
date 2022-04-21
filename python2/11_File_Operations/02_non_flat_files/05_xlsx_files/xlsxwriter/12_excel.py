import xlsxwriter

# By default, xlsxwriter stores all the data in memory for
# for any further cell formmatting; which can lead to memory errors
#  if the holding capacity exceeds.

# The optimization works by flushing each row after a subsequent row is written.


workbook = xlsxwriter.Workbook('memory_ex.xlsx',
                        {'constant_memory': True}
            )
worksheet = workbook.add_worksheet()

row_max = 20
col_max = 6

# # Ok. With 'constant_memory' you must write data in row by column order.
# for row in range(0, row_max):
#     for col in range(0, col_max):
#         worksheet.write(row, col, 'some_data')

# Not ok. With 'constant_memory' this will only write the first column of data.
for col in range(0, col_max):
    for row in range(0, row_max):
        worksheet.write(row, col, 'some_data')

# NOTE: In constant_memory mode the performance should be approximately the same as normal mode.


workbook.close()
