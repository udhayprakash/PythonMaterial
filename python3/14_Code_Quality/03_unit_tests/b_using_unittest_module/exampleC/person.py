class Person:
    """
    >>> p = Person()
    >>> p.set_name('Ram')
    0
    >>> p.get_name(0)
    'Ram'
    >>> user_id = p.set_name('Robert')
    >>> p.get_name(user_id)
    'Robert'
    """

    def __init__(self):
        self.name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id < 0 or user_id >= len(self.name):
            return "There is no such user"
        else:
            return self.name[user_id]
