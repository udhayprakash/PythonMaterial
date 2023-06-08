import re

with open("report.txt") as file:
    file_content = file.read()

result = re.findall(
    r"RowID:\s+(?P<rowid>\d+)\s+Name:\s+(?P<name>[\w, ]+)\n\s+(?P<msg>.*?)(?=\nRowID:|$)",
    file_content,
    re.DOTALL,
)

for rowid, person, msg in result:
    msg = re.sub(r"\n\s+", "", msg)
    print(f"{rowid}, {msg}")

"""
Output:
    100, This person did not meet the criteria because of x,y,z.
    101, This is a warning.This is an error.Criteria was not met.
    103, This person had invalid characters in the email field.

"""
