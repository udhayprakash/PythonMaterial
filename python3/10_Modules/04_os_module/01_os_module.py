#!/usr/bin/python3

import os

# print(dir(os))
#
# ['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL',
#  'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC',
#  'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END',
#  'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__cached__',
#  '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists',
#  '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory',
#  'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull',
#  'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe',
#  'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path',
#  'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid',
#  'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open',
#  'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename',
#  'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle',
#  'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ',
#  'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system',
#  'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom',
#  'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']


print(os.path.basename("/home/user/temp.txt"))  # temp.txt
print(os.path.dirname("/home/user/temp.txt"))  # /home/user
print()

print(os.path.abspath("temp.txt"))  # /home/user/temp.txt
print(os.getcwd())
print()

print(os.path.realpath("/home/user/temp.txt"))
print()

print(os.path.normpath("/path/to/my/../file.txt"))  # "/path/to/file.txt"
print()

print(os.path.splitext("/home/user/temp.log"))  # ('/home/user/temp', '.log')
print(os.path.splitext("temp.log"))  # ('temp', '.log')
print()

print(os.path.splitdrive("/home/user/temp.txt"))  # ('', '/home/user/temp.txt')
print(os.path.splitdrive(r"C:\user\temp.txt"))  # ('C:', '\\user\\temp.txt')
print()

print(os.path.isfile("/home/user/temp.txt"))  # False
print()

print(f"The current directory is: {os.path.abspath('.')}")
print()

print(os.path.extsep)  # .
print(os.sep)  #
