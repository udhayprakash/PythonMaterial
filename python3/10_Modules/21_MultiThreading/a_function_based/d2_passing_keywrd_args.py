"""
Purpose: Passing arguments and keyword arguments,
    to threads
"""
import threading


def my_function(*args, **kwargs):
    thread_name = threading.current_thread().name
    print(f"{thread_name} => args  ={args}")
    print(f"{thread_name} => kwargs={kwargs}")


threading.Thread(name="t1", target=my_function).start()
threading.Thread(name="t2", target=my_function, args=(11, 22)).start()
threading.Thread(
    name="t3", target=my_function, kwargs={"a": "apple", "b": "ball"}
).start()
