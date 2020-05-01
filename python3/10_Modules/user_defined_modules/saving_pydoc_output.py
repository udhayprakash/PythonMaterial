#!/usr/bin/python
"""
Purpose: Generating pydoc documentation
    for custom module
"""

import pydoc
import os 
import sys
from my_module import calculator

# import re

def output_help_to_file(filepath, request):
    with open(filepath, 'w') as f:
        sys.stdout = f
        pydoc.help(request)
        f.close()
    sys.stdout = sys.__stdout__
    return



if __name__ == '__main__':
    if not os.path.exists('docs'):
        os.mkdir('docs')

    output_help_to_file(r'docs/calculator.txt', calculator)

    output_help_to_file(r'docs/re.txt', 're')

    # print(dir(__name__))
    # print()
    # print(__name__.__doc__)

    print(pydoc.help(__name__))
    print()
    print(pydoc.render_doc(__name__))


    with open('docs/__name__.txt', 'w') as a:
        a.write(pydoc.render_doc(__name__))
        a.close()

    output_help_to_file(r'docs/__name__2.txt', calculator)
