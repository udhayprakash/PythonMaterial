"""
Purpose: Union type
"""
from typing import Union


def is_even_whole(num) -> Union[bool, str]:
    if num < 0:
        return "Not a whole number"
    return True if num % 2 == 0 else False


assert is_even_whole(10) is True
assert is_even_whole(19) is False
assert is_even_whole(-2) == "Not a whole number"


def is_even_whole2(num) -> Union[bool, Exception]:
    if num < 0:
        return Exception("Not a whole number")
    return True if num % 2 == 0 else False


assert is_even_whole2(10) is True
assert is_even_whole2(19) is False
res = is_even_whole2(-2)
assert res.args[0] == "Not a whole number"
