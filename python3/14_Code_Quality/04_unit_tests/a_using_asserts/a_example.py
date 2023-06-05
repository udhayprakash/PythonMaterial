"""
Purpose: unit testing using asserts

Symantic:
    assert <statement>, "Error Message, if statement is incorrect"
"""

print(2 + 3 == 5)

assert 2 + 3 == 5
assert 2 + 3 == 5, "2+ 3 is Not resulting to 5"


print(2 + 3 == 6)
try:
    assert 2 + 3 == 6, "2+ 3 is Not resulting to 6"
except AssertionError as ex:
    print(ex)


try:
    assert 10 - 34 > 3
except AssertionError as ex:
    print(f"Error is {ex}")


try:
    assert 10 - 34 > 3, "This statement is incorrect"
except AssertionError as ex:
    print(f"Error is {ex}")


assert 1 == True
assert "1" != str(True)
