class subject:
    count = 0

    def __init__(self, name):
        self.name = name

    def set(self, name):
        self._name = name

    def get(self):
        return self._name

    name = property(get, set)


s = subject("udhay")
