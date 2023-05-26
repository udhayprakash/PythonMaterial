data = [
    "Date|Transaction Type|Amount|Description",
    "2022-01-01|Income|5000.00|Salary",
    "2022-01-02|Expense|150.50|Groceries",
    "2022-01-03|Expense|35.75|Transportation",
    "2022-01-04|Income|2000.00|Investment Dividends",
    "2022-01-05|Expense|50.00|Entertainment",
    "2022-01-06|Expense|1000.00|Rent",
]

# Create the .dat file
with open("sample.dat", "w") as file:
    file.write("\n".join(data))


# Read the .dat file
with open("sample.dat", "r") as file:
    data = file.read().splitlines()

for row in data:
    print(row.split("|"))
