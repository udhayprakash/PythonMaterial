import re

def validate_only_lower_case_letters(to_validate):
    pattern = r'^[a-z]+$'
    return bool(re.match(pattern, to_validate))

print(validate_only_lower_case_letters('thisshouldbeok'))
print(validate_only_lower_case_letters('thisshould notbeok'))
print(validate_only_lower_case_letters('Thisshouldnotbeok'))
print(validate_only_lower_case_letters('thisshouldnotbeok1'))
print(validate_only_lower_case_letters(''))