import ctypes

value3 = 100

# Getting address of variable
memory_addr2 = id(value3)  
print("value 3 =", value3)
print("Memory addr (INT) =", memory_addr2)

# Integer to hex conversion
memory_addr3 = hex(memory_addr2)
print("Memory addr (HEX) =", memory_addr3)

# Revert to Integer Type from hex
memory_addr4 = int(memory_addr3, base=16)
print("Memory addr (INT) =", memory_addr4)

# Getting value of addr
value4 = ctypes.cast(memory_addr4, ctypes.py_object).value
print("value 4 =", value4)
