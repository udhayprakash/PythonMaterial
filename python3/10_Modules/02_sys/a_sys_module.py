import sys

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
