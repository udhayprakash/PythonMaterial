from functools import wraps

def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "How about party today?"
    return msg, say_please


print(say())  # How about party today?
print(say(say_please=True))  # How about party today? Please! I am poor :(
