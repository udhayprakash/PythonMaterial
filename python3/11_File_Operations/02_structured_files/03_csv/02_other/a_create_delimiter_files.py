import csv

data = [
    ["Date", "Transaction Type", "Amount", "Description"],
    ["2022-01-01", "Income", 5000.00, "Salary"],
    ["2022-01-02", "Expense", 150.50, "Groceries"],
    ["2022-01-03", "Expense", 35.75, "Transportation"],
    ["2022-01-04", "Income", 2000.00, "Investment Dividends"],
    ["2022-01-05", "Expense", 50.00, "Entertainment"],
    ["2022-01-06", "Expense", 1000.00, "Rent"],
]

# CSV (Comma-Separated Values) - Create the CSV file
with open("sample.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# TSV (Tab-Separated Values) - Create the TSV file
with open("sample.tsv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(data)

# SSV (Semicolon-Separated Values) - Create the SSV file
with open("sample.ssv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(data)

# PSV (Pipe-Separated Values) - Create the PSV file
with open("sample.psv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="|")
    writer.writerows(data)

# DSV (Delimiter-Separated Values) - Create the DSV file
with open("sample.dsv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="#")
    writer.writerows(data)
