#!/usr/bin/python
"""
Purpose: Functions Demo

    Function with Keyword ONLY args

    Named arguments appearing after '*' can only be 
    passed by keyword

    Present only in Python 3.X
"""
def servr_login(server_name, user_name, password):
    print(f'''
        {server_name =}
        {user_name   =}
        {password    =}
    ''')

servr_login('facebook.com', 'udhay', 'udhay123')
servr_login('facebook.com', 'udhay123', 'udhay')


def servr_login(server_name, *, user_name, password):
    print(f'''
        {server_name =}
        {user_name   =}
        {password    =}
    ''')

servr_login('facebook.com', user_name='udhay', password='udhay123')
# servr_login('facebook.com', 'udhay123', 'udhay')
# TypeError: servr_login() takes 1 positional argument but 3 were given


# Function Definition
def recv(maxsize, *,  block=True):
    print("\ntype(maxsize)  ", type(maxsize))
    print("type(block) ", type(block))

    print("maxsize   " + str(maxsize))
    print("block     " + str(block))
    print('-' * 20)


# Function Call 
recv(1234)
recv(maxsize=1234, block=False)
recv(1234, block=False)


# recv(1234, False) # TypeError: recv() takes 1 positional argument but 2 were given

"""
 Recommended order for the arguments
    def func(positional, keyword=value, *args, **kwargs):
        pass
"""