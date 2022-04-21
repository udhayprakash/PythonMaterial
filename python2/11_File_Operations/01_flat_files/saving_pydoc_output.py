import sys
import pydoc
import example
#import re

"""
This is the first line.

This is second line.
This is third line
fourth
fifth
"""
def output_help_to_file(filepath, request):
    f = file(filepath, 'w')
    sys.stdout = f
    pydoc.help(request)
    f.close()
    sys.stdout = sys.__stdout__
    return

output_help_to_file('newfile.txt', example)

# #output_help_to_file(r'test.txt', 're')

# print dir(__name__)
# #print __name__.__doc__

# #print pydoc.help(__name__)

# print pydoc.render_doc(__name__)

# with open('file1.txt','wb') as a:
# 	a.write(pydoc.render_doc(__name__))
# 	a.close()

# with open('file2.txt','wb') as a:
# 	sys.stdout = a
# 	pydoc.render_doc(__name__)
# 	sys.stdout = sys.__stdout__
# 	a.close()
