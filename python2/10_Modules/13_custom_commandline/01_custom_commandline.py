from cmd import Cmd

class MyPrompt(Cmd):
    pass

p = MyPrompt()
p.cmdloop()

"""
USAGE:
    (Cmd) dir
    *** Unknown syntax: dir
    (Cmd) ls
    *** Unknown syntax: ls
    (Cmd) help

    Documented commands (type help <topic>):
    ========================================
    help

    (Cmd) help cmd
    *** No help on cmd
"""
