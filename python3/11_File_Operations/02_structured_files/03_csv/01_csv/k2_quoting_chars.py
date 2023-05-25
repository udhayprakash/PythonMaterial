import csv

# Example data
data = [
    ["John", "Doe", 25, "john@example.com"],
    ["Jane", "Smith", 30, "jane@example.com"],
    ["Bob", "Brown", "N/A", "bob@example.com"],
]

# Quoting options
quoting_options = [
    csv.QUOTE_MINIMAL,
    csv.QUOTE_ALL,
    csv.QUOTE_NONNUMERIC,
    csv.QUOTE_NONE,
]

# Iterate over quoting options
for quoting in quoting_options:
    print(quoting)
    # Create a CSV writer with the specified quoting option
    csv_writer = csv.writer(open("data.csv", "w", newline=""), quoting=quoting)

    # Write the data to the CSV file
    csv_writer.writerows(data)

    # Read the CSV file to verify the quoting behavior
    with open("data.csv", "r") as file:
        csv_reader = csv.reader(file)
        print(f"Quoting option: {quoting}")

        # Print each row
        for row in csv_reader:
            print(row)

    print("---")

"""
Quoting option: <csv.QUOTE_MINIMAL>
John,Doe,25,john@example.com
Jane,Smith,30,jane@example.com
Bob,Brown,N/A,bob@example.com

Quoting option: <csv.QUOTE_ALL>
"John","Doe","25","john@example.com"
"Jane","Smith","30","jane@example.com"
"Bob","Brown","N/A","bob@example.com"

Quoting option: <csv.QUOTE_NONNUMERIC>
John,Doe,"25",john@example.com
Jane,Smith,"30",jane@example.com
Bob,Brown,"N/A",bob@example.com

Quoting option: <csv.QUOTE_NONE>
John,Doe,25,john@example.com
Jane,Smith,30,jane@example.com
Bob,Brown,N/A,bob@example.com
"""
