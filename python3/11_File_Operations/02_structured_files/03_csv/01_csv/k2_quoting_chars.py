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
    file_name = f"data_{str(quoting)}.csv"
    with open(file_name, "w", newline="") as fh:
        writer= csv.writer(fh,  quoting=quoting)
        # Write the data to the CSV file
        writer.writerows(data)

    # Read the CSV file to verify the quoting behavior
    with open(file_name, "r") as file:
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
