import xlsxwriter

workbook = xlsxwriter.Workbook('Expenses01.xlsx')

worksheet = workbook.add_worksheet()

expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

row, col = 0, 0
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1


# write total using formula 
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()
