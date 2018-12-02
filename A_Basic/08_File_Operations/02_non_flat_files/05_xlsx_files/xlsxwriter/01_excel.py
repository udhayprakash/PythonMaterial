import xlsxwriter

with xlsxwriter.Workbook('hello.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Hello World')

    workbook.close()