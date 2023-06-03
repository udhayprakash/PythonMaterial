"""
Purpose: Perl compatible regex substitution
"""

import re

text = """

hello  hello
goodbye
bye   bye bye
hello goodbye
"""

# To remove duplicate words, linewise
pat = re.compile(r"(?P<word>\S*) (\s+(?P=word)) +\s*$", re.MULTILINE)
result = pat.sub("\g<word>", text)
print(result)
