from unittest.mock import MagicMock

class SomeClass:
    pass 

real = SomeClass()
real.method = MagicMock(name='method')
real.method(3, 4, 5, key='value') # <MagicMock name='method()' id='...'>

# --------------------------------------------------------
class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        pass

real = ProductionClass()
real.something = MagicMock()
real.method()
real.something.assert_called_once_with(1, 2, 3)

# -----------------------------------------------------------
# In [1]: from unittest.mock import Mock, MagicMock, ANY
# In [2]: mock = Mock()
# In [3]: magic = MagicMock()
# In [4]: mock.foo == ANY
# Out[4]: True
# In [5]: magic.foo == ANY
# Out[5]: False