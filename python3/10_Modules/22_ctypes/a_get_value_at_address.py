import ctypes

name = "Udhay Prakash"
address = id(name)

# Retriveing value at the address location
value = ctypes.cast(address, ctypes.py_object).value

print(f"{name    = }")
print(f"{address = }")
print(f"{value   = }")
