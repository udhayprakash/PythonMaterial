#!/usr/bin/python3
"""
Purpose: Iterating over Dictionaries
"""
person_details = {
    "name": "Narendra Modi",
    "age": 67,
    "salary": 2_00_000,
    "role": "CM of Gujarat",
    "role": "PM of India",  # latest will be stored
}

print(person_details)

# To get the dictionary keys
print(f"{person_details.keys()  =}")

# To get the dictionary keys
print(f"{person_details.values() =}")

# To get both keys & values as pairs
print(f"{person_details.items() =}")

print("\n Iterating over the dictionary ")
for each in person_details:
    print(each)

# NOTE: By default, when iterating over dict, it will give dict keys only
print("\n person_details.keys()")
for each in person_details.keys():
    print(each)

print("\n person_details.values()")
for each in person_details.values():
    print(each)

print("\n person_details.items()")
for each in person_details.items():
    print(each)  # each - is a tuple object

print("\n person_details.items()")
for each_key, each_value in person_details.items():
    print(f"{each_key}\t{each_value}")
