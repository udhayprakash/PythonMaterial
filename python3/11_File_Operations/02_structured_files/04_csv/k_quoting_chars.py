#!/usr/bin/python
"""
Purpose: Writing csv

"""
import csv

with open('k_delimiter_pipe.csv', 'w', newline='', encoding='utf-8') as gh:
    header_names = ('sno', 'name', 'language')
    writer = csv.writer(gh, delimiter='|', dialect='excel')

    # To write the headers
    writer.writerow(header_names)

    writer.writerow([1, 'english', 'Python'])
    writer.writerows([
        [2, 'Russian', 'питон'],
        [3, 'Italian', 'Pitone'],
        [4, 'Japanese', 'パイソン'],
        [5, 'Chinese', '蟒蛇'],
        [6, 'Telugu', 'పైథాన్'],
        [7, 'Tamil', 'பைதான்'],
        [8, 'Hindi', 'अजगर'],
    ])
    gh.close()


print(f'{csv.list_dialects() =}')  # ['excel', 'excel-tab', 'unix']
# For excel dielect, default delimiter is ,
# For excel-tab dielect, default delimiter is \t

# To get current maximum field size allowed by the parser
print(f'{csv.field_size_limit() =}')


'''
Formatting a csv file
-----------------------
- quotechar
    - a one-character string to use as the quoting character.
    - It defaults to '"'.
    - Setting this to None has the same effect as setting quoting to csv.QUOTE_NONE.
- delimiter
    - a one-character string to use as the field separator.
    - It defaults to ','.
- escapechar
    - a one-character string used to escape the delimiter when quotechar is set to None.
- skipinitialspace
    - how to interpret whitespace which immediately follows a delimiter.
    - It defaults to False, which means that whitespace immediately following a delimiter is part of the following field.
- lineterminator
    - the character sequence which should terminate rows.
- quoting controls when quotes should be generated by the writer. It can take on any of the following module constants:
    - csv.QUOTE_MINIMAL means only when required, for example, when a field contains either the quotechar or the delimiter
    - csv.QUOTE_ALL means that quotes are always placed around fields.
    - csv.QUOTE_NONNUMERIC means that quotes are always placed around nonnumeric fields.
    - csv.QUOTE_NONE means that quotes are never placed around fields.
- doublequote controls the handling of quotes inside fields.
    - When True two consecutive quotes are interpreted as one during read, and when writing, each quote is written as two quotes.
'''
