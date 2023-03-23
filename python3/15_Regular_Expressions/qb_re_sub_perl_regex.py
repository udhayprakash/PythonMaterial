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
pat = re.compile(r"^(?P<x>\S*) (\s+(?P=x)) +\s*$", re.MULTILINE)
result = pat.sub("\g<x>", text)
print(result)
