#!/usr/bin/python
"""
Purpose: Base 64 encoding
"""
import base64

# takes byte-string only
encoded = base64.b64encode(b"data to be encoded")
print(f"encoded     : {encoded}")

original_msg = base64.b64decode(encoded)
print(f"original_msg: {original_msg}")

encoded = base64.b64encode("data to be encoded".encode("utf-8"))
print(f"encoded     : {encoded}")

original_msg = base64.b64decode(encoded)
print(f"original_msg: {original_msg}")
