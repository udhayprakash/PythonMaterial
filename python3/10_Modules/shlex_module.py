#!/usr/bin/python
"""
Purpose: shlex Module 
    - built-in module 
    - for Lexical analysis of shell-style syntaxes
"""
import shlex


def get_word_tokens(sentence):
    print('\n\n', sentence)
    print('\nTOKENS:')
    lexer = shlex.shlex(sentence)
    for token in lexer:
        print('\t', repr(token))

sentence1 = '''
    This string has embedded "double quotes" and 'single quotes' in it,
    and even "a 'nested example'". 
    '''
get_word_tokens(sentence1)


sentence2 = ''' This string has an embedded apostrophe, doesn't it? '''
get_word_tokens(sentence2)


embedded_comments_text = 'This line is recognized.\n# But this line is ignored.\nAnd this line is processed.' 
get_word_tokens(embedded_comments_text)
# NOTE: Observe that commented line is ignored


# --------------
text = """This text has "quoted parts" inside it."""
print('\n\nORIGINAL TEXT:\n\t', text)
print('COMPONENT TOKENS:\n\t', shlex.split(text))


# Controlling the Parser
text = """|Col 1||Col 2||Col 3|"""
print('\n\nORIGINAL:', repr(text))

lexer = shlex.shlex(text)
lexer.quotes = '|'

print('TOKENS:')
for token in lexer:
    print('\t', repr(token))

# NOTE: Each quote must be a single character, 
#   so it is not possible to have different open and close quotes 
#   (no parsing on parentheses, for example).


# POSIX vs. Non-POSIX Parsing
for s in ( 'Do"Not"Separate',
           '"Do"Separate',
           'Escaped \e Character not in quotes',
           'Escaped "\e" Character in double quotes',
           "Escaped '\e' Character in single quotes",
           r"Escaped '\'' \"\'\" single quote",
           r'Escaped "\"" \'\"\' double quote',
           "\"'Strip extra layer of quotes'\""):
    print('\nORIGINAL :', repr(s))
    print('non-POSIX:', end = '')

    non_posix_lexer = shlex.shlex(s, posix=False)
    try:
        print(repr(list(non_posix_lexer)))
    except ValueError as err:
        print('error(%s)' % err)

    
    print('POSIX    :', end=' ')
    posix_lexer = shlex.shlex(s, posix=True)
    try:
        print(repr(list(posix_lexer)))
    except ValueError as err:
        print('error(%s)' % err)
