#!/usr/bin/python
"""
Purpose: Getting Command-line arguments
"""
import sys

print(f'{__file__ =}')
print(f'{sys.argv =}')

assert __file__ == sys.argv[0]

'''
~python l_command_line_args.py
__file__ ='l_command_line_args.py'
sys.argv =['l_command_line_args.py']

~python ..\03_sys_module\l_command_line_args.py
__file__ ='..\\03_sys_module\\l_command_line_args.py'
sys.argv =['..\\03_sys_module\\l_command_line_args.py']

~python ..\..\10_Modules\03_sys_module\l_command_line_args.py
__file__ ='..\\..\\10_Modules\\03_sys_module\\l_command_line_args.py'   
sys.argv =['..\\..\\10_Modules\\03_sys_module\\l_command_line_args.py'] 

~python D:\MEGAsync\Python-related\training\python_related\python_batch154\10_Modules\03_sys_module\l_command_line_args.py
__file__ ='D:\\MEGAsync\\Python-related\\training\\python_related\\python_batch154\\10_Modules\\03_sys_module\\l_command_line_args.py'
sys.argv =['D:\\MEGAsync\\Python-related\\training\\python_related\\python_batch154\\10_Modules\\03_sys_module\\l_command_line_args.py'] 

~python l_command_line_args.py apple 123 12.23 True False None
__file__ ='l_command_line_args.py'
sys.argv =['l_command_line_args.py', 'apple', '123', '12.23', 'True', 'False', 'None']      

'''
