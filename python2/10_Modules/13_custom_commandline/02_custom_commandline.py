from cmd import Cmd

class MyPrompt(Cmd):
   def do_exit(self, inp):
        '''exit the application.'''
        print('Bye')
        return True

   def do_add(self, inp):
        print("Adding '{}'".format(inp))

   def help_add(self):
       print('Add a new entry to the system.')

MyPrompt().cmdloop()

"""
USAGE
    (Cmd) ?

    Documented commands (type help <topic>):
    ========================================add  exit  help
    (Cmd) help
    Documented commands (type help <topic>):
    ========================================
    add  exit  help

    (Cmd) help add
    Add a new entry to the system.
    (Cmd) help help
    List available commands with "help" or detailed help with "help cmd".
    (Cmd) help exit
    exit the application.
    (Cmd) add 123
    Adding '123'
    (Cmd) exit                                                                    plete_hBye                                                                           'doc_le
"""
