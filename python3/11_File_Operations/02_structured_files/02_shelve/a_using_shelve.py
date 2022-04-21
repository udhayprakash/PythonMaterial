#!/usr/bin/python
"""
Purpose: using shelve
    stores in .db files
"""
import shelve

# creating a new shelve file
s = shelve.open("michelShelve.db")
s["key1"] = {"int": 10, "float": 9.5, "string": "Sample data"}
s.close()

# To access the data again, open the shelve and use it like a dictionary
s = shelve.open("michelShelve.db")
existing = s["key1"]
print(existing)
s.close()


# ---------------\
# By defaults, shelve do not track modifications to volatile objects.
s = shelve.open("michelShelve.db")
print("before", s["key1"])
s["key1"]["new_value"] = "this was not here before"
print("after", s["key1"])
s.close()


s = shelve.open("michelShelve.db")
print(s["key1"])  # modifications are not reflected
s.close()

# To automatically catch the changes, open the shelve with writeback enabled
s = shelve.open("michelShelve.db", writeback=True)
print("before", s["key1"])
s["key1"]["new_value"] = "this was not here before"
print("after", s["key1"])

s.close()

s = shelve.open("michelShelve.db", writeback=True)
print(s["key1"])
s.close()

# Note: Shelve must not be opened with writeback enabled,
# unless it is essential
