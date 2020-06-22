import sys
from pprint import pprint

# pprint(vars(sys))

print(f''' 
    {sys.maxsize                    =}
    {sys.maxunicode                 =}
    {sys.platform                   =}
    {sys.byteorder                  =}
    {sys.dllhandle                  =}
    {sys.float_repr_style           =}

    {sys.argv                       =}
    {sys.executable                 =}
    {sys.dont_write_bytecode        =}
    {sys.hash_info                  =}
    {sys.hexversion                 =}
    {sys.getrecursionlimit()        =}
    
    {sys.base_exec_prefix           =}
    {sys.base_prefix                =}
    {sys.exec_prefix                =}
    {sys.prefix                     =}
    {sys.pycache_prefix             =}
    
    {sys.flags                      =}
    {sys.exc_info()                 =}

    {sys.getallocatedblocks()       =}
    {sys.getcheckinterval()         =}
    {sys.getdefaultencoding()       =}
    {sys.getfilesystemencodeerrors()=}
    {sys.getfilesystemencoding()    =}
    {sys.getprofile()               =}
    {sys.getswitchinterval()        =}
    {sys.getrefcount                =}

    {sys.getsizeof                  =}
    {sys.audit                      =}
    {sys.displayhook                =}
    {sys.int_info                   =}
    {sys.intern                     =}
    {sys.setcheckinterval           =}
    {sys.setprofile                 =}
    {sys.setrecursionlimit          =}
    {sys.setswitchinterval          =}
    {sys.stderr                     =}
    {sys.stdin                      =}
    {sys.stdout                     =}
    {sys.thread_info                =}
    {sys.warnoptions                =}
''')
# {sys.builtin_module_names       =}
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