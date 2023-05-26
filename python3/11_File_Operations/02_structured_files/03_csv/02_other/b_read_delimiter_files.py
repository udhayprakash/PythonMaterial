import csv

# CSV (Comma-Separated Values) - Read the CSV file
with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# TSV (Tab-Separated Values) - Read the TSV file
with open("sample.tsv", "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        print(row)

# SSV (Semicolon-Separated Values) - Read the SSV file
with open("sample.ssv", "r") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)

# PSV (Pipe-Separated Values) - Read the PSV file
with open("sample.psv", "r") as file:
    reader = csv.reader(file, delimiter="|")
    for row in reader:
        print(row)

# DSV (Delimiter-Separated Values) - Read the DSV file
with open("sample.dsv", "r") as file:
    reader = csv.reader(file, delimiter="#")
    for row in reader:
        print(row)
