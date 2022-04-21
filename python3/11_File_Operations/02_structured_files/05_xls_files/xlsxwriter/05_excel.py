from datetime import datetime
import xlsxwriter

with xlsxwriter.Workbook("Expenses03.xlsx") as wb:
    ws = wb.add_worksheet()

    bold = wb.add_format({"bold": 1})
    money_format = wb.add_format({"num_format": "$#,##0"})
    date_format = wb.add_format({"num_format": "mmmm d yyyy"})

    # Adjust column width
    ws.set_column(1, 1, 15)

    ws.write("A1", "Item", bold)
    ws.write("B1", "Date", bold)
    ws.write("C1", "Cost", bold)

    expenses = (
        ["Rent", "2013-01-13", 1000],
        ["Gas", "2013-01-14", 100],
        ["Food", "2013-01-16", 300],
        ["Gym", "2013-01-20", 50],
    )

    row, col = 1, 0

    for item, date_str, cost in expenses:
        # Convert the date string into a datetime object.
        date = datetime.strptime(date_str, "%Y-%m-%d")

        ws.write_string(row, col, item)
        ws.write_datetime(row, col + 1, date, date_format)
        ws.write_number(row, col + 2, cost, money_format)
        row += 1

    # Write a total using a formula.
    ws.write(row, 0, "Total", bold)
    ws.write(row, 2, "=SUM(C2:C5)", money_format)

    wb.close()
