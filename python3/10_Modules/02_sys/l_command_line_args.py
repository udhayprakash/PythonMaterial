#!/usr/bin/python3
"""
Purpose: Getting Command-line arguments
"""
import sys

print("__file__", __file__)
print("sys.argv", sys.argv[0])
print("__file__", __file__.replace("\\", "/"))

assert __file__ != sys.argv[0]
# assert __file__.replace('\\', '/') != sys.argv[0]
r"""
python .\l_command_line_args.py
    __file__ 10_Modules\02_sys\l_command_line_args.py
    sys.argv ['.\\l_command_line_args.py']

 python .\02_sys\l_command_line_args.py
    __file__ 10_Modules\02_sys\l_command_line_args.py
    sys.argv ['.\\02_sys\\l_command_line_args.py']

 python .\10_Modules\02_sys\l_command_line_args.py
    __file__ 10_Modules\02_sys\l_command_line_args.py
    sys.argv ['.\\10_Modules\\02_sys\\l_command_line_args.py']

python .\10_Modules\02_sys\l_command_line_args.py 10 True something 213.2
    __file__ 10_Modules\02_sys\l_command_line_args.py
    sys.argv ['.\\10_Modules\\02_sys\\l_command_line_args.py', '10', 'True', 'something', '213.2']

"""
