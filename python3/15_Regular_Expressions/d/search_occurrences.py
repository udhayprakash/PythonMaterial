import re

secret_code = 'qwret 8sfg12f5 fd09f_df'
# "r" at the beginning means raw format, use it with regular expression patterns
search_pattern = r'(g12)'

match = re.search(search_pattern, secret_code)
print('match: {}'.format(match))
print('match.group(): {}'.format(match.group()))

numbers_pattern = r'[0-9]'
numbers_match = re.findall(numbers_pattern, secret_code)
print('numbers: {}'.format(numbers_match))
