"""
purpose: regular expression

    re.split
"""
import re

print(re.findall(".", "244.255.190.23"))
print()

print(re.findall("\.", "244.255.190.23"))
print(re.findall("[.]", "244.255.190.23"))
print()

print(re.split("\.", "244.255.190.23"))
print(re.split("[.]", "244.255.190.23"))
print()

print(re.split("[.]", "244.255.190.23", 0))  # ['244', '255', '190', '23']
print(re.split("[.]", "244.255.190.23", maxsplit=1))  # ['244', '255.190.23']
print(re.split("[.]", "244.255.190.23", maxsplit=2))  # ['244', '255', '190.23']
print(re.split("[.]", "244.255.190.23", 3))  # ['244', '255', '190', '23']
print(re.split("[.]", "244.255.190.23", 4))  # ['244', '255', '190', '23']
print(re.split("[.]", "244.255.190.23", 5))  # ['244', '255', '190', '23']
print()

print(re.split(r"\s", "Hello World! This is a sentence."))
print()

print(re.split(r",", "apple,banana,orange,grape"))
print(re.split(r"(,)", "apple,banana,orange,grape"))  # retains , too

print("\n Splitting and excluding the delimiter")
print(re.split(r"(?<=,)", "apple,banana,orange,grape"))

print()

print("\n Splitting by multiple delimiters")
print(re.split(r"[,\s;-]", "apple, banana; orange - grape"))
print(re.split(r"\d+", "apple, banana; orange - grape"))
print()
