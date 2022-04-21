import xlsxwriter

with xlsxwriter.Workbook("Expenses02.xlsx") as wb:
    worksheet = wb.add_worksheet()

    # creating cell formats
    bold = wb.add_format({"bold": True})
    money = wb.add_format({"num_format": "$#,##0"})

    worksheet.write("A1", "Item", bold)
    worksheet.write("B1", "Cost", money)

    expenses = (
        ["Rent", 1000],
        ["Gas", 100],
        ["Food", 300],
        ["Gym", 50],
    )

    # write(row, column, token, [format])
    row, col = 1, 0
    for item, cost in expenses:
        worksheet.write(row, col, item)
        worksheet.write(row, col + 1, cost, money)
        row += 1

    worksheet.write(row, 0, "Total", bold)
    worksheet.write(row, 1, "=SUM(B2:B5)", money)

    wb.close()
