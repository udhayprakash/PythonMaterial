#!/usr/bin/python3
"""
Purpose: sys module 
"""
import sys 
print(dir(sys))


print(f''' 
    {sys.winver             =}
    {sys.version            =}
    {sys.version_info       =}
    {sys.getwindowsversion()=}
    {sys.implementation     =}

    {sys.api_version        =}
    {sys.is_finalizing()    =}

    sys.copyright           =\n{sys.copyright}
''')


# cpython -c      python.org
# Jython  - Java  
# Ironthon- dotnet