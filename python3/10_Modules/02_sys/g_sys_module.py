#!/usr/bin/python
"""
Purpose: sys module 
"""
import sys 
from pprint import pprint
print(f''' 
    {sys.audit                      =}
    {sys.displayhook                =}
    {sys.int_info                   =}
    {sys.intern                     =}
    {sys.thread_info                =}
    {sys.warnoptions                =}

    {sys.builtin_module_names       =}
''')

pprint(sys.modules)

# {sys.call_tracing               =}
# {sys.callstats                  =}


# gettrace
# settrace
# get_asyncgen_hooks
# get_coroutine_origin_tracking_depth
# set_asyncgen_hooks
# set_coroutine_origin_tracking_depth

# modules

# path_hooks
# path_importer_cache

# unraisablehook


# For customizing python prompt - https://arpitbhayani.me/blogs/python-prompts