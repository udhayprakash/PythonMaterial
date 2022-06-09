class Customer:

    def __init__(self, cust_id, level=0):
        self._cust_id = cust_id
        self._level = level

    def __str__(self):
        return f'< Customer cust_id = {self._cust_id}, level = {self._level} >'

    @property 
    def cust_id(self):
        return self._cust_id

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1

    def level_down(self):
        self._level -= 1 if self._level >= 1 else self._level
