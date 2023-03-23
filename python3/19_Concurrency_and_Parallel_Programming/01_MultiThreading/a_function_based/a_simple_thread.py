"""
Purpose:
    A user defined function is created and
    the function is called when a thread is initialized.


"""
import threading

# print(dir(threading))
# help(threading)


def hello_world():
    """This is a user defined function"""
    print("Hello World")


# Method 1- Sequential
# hello_world()

# Method 2 - Using multithreading
# Initializing a thread
my_thread = threading.Thread(target=hello_world)

# Starting a thread
my_thread.start()
