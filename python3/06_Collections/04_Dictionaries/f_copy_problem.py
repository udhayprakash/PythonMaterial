#!/usr/bin/python3
"""
Purpose: Dictionaries
    Memory leakage issue
"""
import copy

signup_form = {"name": "Udhay", "age": 31, "height": 169, "weight": 73}

# assignment operation
new_signup_form = signup_form

print("\n After assignment")
print(signup_form)
print(new_signup_form)


# leakageIssue
new_signup_form["name"] = "Dhoni"

print("\n after change")
print(signup_form)
print(new_signup_form)

print(f"{id(signup_form)     =}")
print(f"{id(new_signup_form) =}")

del signup_form
del new_signup_form

# ----------------------------------------
# Solution
print()
signup_form = {"name": "Udhay", "age": 31, "height": 169, "weight": 73}
new_signup_form = signup_form.copy()

print("\n using dict.copy()")
new_signup_form["name"] = "Dhoni"

print(signup_form)
print(new_signup_form)
print(f"{id(signup_form)     =}")
print(f"{id(new_signup_form) =}")

del signup_form
del new_signup_form

# -----------------------------------
signup_form = {"name": "Udhay", "age": 31, "health": {"height": 169, "weight": 73}}
new_signup_form = copy.deepcopy(signup_form)

print("\n using copy.deepcopy()")
new_signup_form["health"]["weight"] = 82

print(signup_form)
print(new_signup_form)
print(f"{id(signup_form)     =}")
print(f"{id(new_signup_form) =}")
