import csv

data = [
    ("sno", "country", "city"),
    ("1", "UK", "London"),
    ("2", "UK", "manchester"),
    ("3", "USA", "california"),
]

with open("csvfile.csv", "w") as csvOutput:
    writer = csv.writer(
        csvOutput,
        delimiter="|",
        escapechar=" ",
        quoting=csv.QUOTE_NONE,
        lineterminator="\n",
    )

    for row in data:
        writer.writerow([s.replace("\n", "\\n") for s in row])
