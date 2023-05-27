import pickle
import socket
import sqlite3


def try_pickle(obj):
    try:
        pickle.dumps(obj)
        print(f"{type(obj).__name__:12} can be pickled.")
    except (pickle.PicklingError, TypeError) as e:
        print(f"{type(obj).__name__:12} cannot be pickled. Error: {str(e)}")


# Objects that cannot be pickled
objects = [
    socket.socket(),  # Network connections (socket)
    sqlite3.connect(":memory:"),  # Database connections
    lambda x: x + 1,  # Lambda functions
    (x for x in range(10)),  # Generator objects
    open("data.pickle", "r"),  # File objects
]

# Attempt to pickle each object
for obj in objects:
    try_pickle(obj)
