from unittest.mock import Mock

m = Mock()
# Mocks by default create new attributes out of a thin air
m.not_existing_attribute  # <Mock name='mock.not_existing_attribute' id='140507980563984'>

# Calling Mocks returns by default another Mock instance
m.not_existing_attribute()  # <Mock name='mock.not_existing_attribute()' id='140507980625760'>

# once created, auto-created attribute is kept and we keep on getting it
m.not_existing_attribute()  # <Mock name='mock.not_existing_attribute()' id='140507980625760'>
