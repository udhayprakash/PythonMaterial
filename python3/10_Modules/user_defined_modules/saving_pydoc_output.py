#!/usr/bin/python
"""
Purpose: Generating pydoc documentation
    for custom module
"""

import os
import pydoc
import sys

from my_package import calculator


def output_help_to_file(filepath, request):
    with open(filepath, "w") as f:
        sys.stdout = f
        pydoc.help(request)
        f.close()
    sys.stdout = sys.__stdout__
    return


if __name__ == "__main__":
    if not os.path.exists("docs"):
        os.mkdir("docs")

    output_help_to_file(r"docs/calculator.txt", calculator)
    output_help_to_file(r"docs/math.txt", "math")

    # print(dir(__name__))
    # print()
    # print(__name__.__doc__)

    print(pydoc.help(__name__))
    print()
    print(pydoc.render_doc(__name__))

    with open("docs/__name__.txt", "w") as a:
        a.write(pydoc.render_doc(__name__))
        a.close()
