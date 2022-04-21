#!/usr/bin/python

"""
Purpose: Discussion on unicode strings
    Ref: https://docs.python.org/3/howto/unicode.html

ASCII - english only

ENCODING: Unicode string is a sequence of code points,
    which are numbers from 0 through 0x10FFFF (1,114,111 decimal).
    This sequence needs to be represented as a set of bytes (meaning,
    values from 0 through 255) in memory. The rules for translating a
    Unicode string into a sequence of bytes are called an encoding.

RULES of converting Unicode string to ASCII encoding
----------------------------------------------------
for each code point:
    - If the code point is < 128, each byte is the same as the value of the code point.
    - If the code point is 128 or greater, the Unicode string can’t be represented in this encoding.
    (Python raises a UnicodeEncodeError exception in this case.)

UTF - Unicode Transformation Format
UTF-8 - 8-bit numbers

UTF-8 uses the following rules:
    - If the code point is < 128, it’s represented by the corresponding byte value.
    - If the code point is >= 128, it’s turned into a sequence of two, three, or four bytes, where each byte of the sequence is between 128 and 255.
UTF-8 has several convenient properties:

It can handle any Unicode code point.
    - A Unicode string is turned into a sequence of bytes containing no embedded zero bytes. This avoids byte-ordering issues, and means UTF-8 strings can be processed by C functions such as strcpy() and sent through protocols that can’t handle zero bytes.
    - A string of ASCII text is also valid UTF-8 text.
    - UTF-8 is fairly compact; the majority of commonly used characters can be represented with one or two bytes.
    - If bytes are corrupted or lost, it’s possible to determine the start of the next UTF-8-encoded code point and resynchronize. It’s also unlikely that random 8-bit data will look like valid UTF-8.

python 2 - default encoding - ascii
python 3 - default encoding - unicode

Different encoding can be specified by placing the below line in the first line of script:
# -*- coding: <encoding name> -*-

"""
import unicodedata

print("\N{GREEK CAPITAL LETTER DELTA}")  # '\u0394' - Using the character name
print("\u0394")  # '\u0394' - Using a 16-bit hex value
print("\U00000394")  # '\u0394' - Using a 32-bit hex value

# b'\x80abc'.decode("utf-8", "strict")
#  UnicodeDecodeError: 'utf-8' codec can't decode
#      byte 0x80 in position 0: invalid start byte

print(b"\x80abc".decode("utf-8", "replace"))  # '\ufffdabc'
print(b"\x80abc".decode("utf-8", "backslashreplace"))  # '\\x80abc'
print(b"\x80abc".decode("utf-8", "ignore"))  # 'abc'

# list of encoding standards supported in python
# https://docs.python.org/3/library/codecs.html#standard-encodings

# One-character Unicode strings can also be created with the chr() built-in function
print(chr(57344))  # '\ue000'
print(ord("\ue000"))  # 57344

# unicode to bytes
u = chr(40960) + "abcd" + chr(1972)
print(u, type(u))

print(u.encode("utf-8"))  # b'\xea\x80\x80abcd\xde\xb4'
# >>> u.encode('ascii')
# Traceback (most recent call last):
#     ...
# UnicodeEncodeError: 'ascii' codec can't encode character '\ua000' in
#   position 0: ordinal not in range(128)

print(u.encode("ascii", "ignore"))  # b'abcd'
print(u.encode("ascii", "replace"))  # b'?abcd?'
print(u.encode("ascii", "xmlcharrefreplace"))  # b'&#40960;abcd&#1972;'
# b'\\ua000abcd\\u07b4' (inserts a \uNNNN escape sequence)
print(u.encode("ascii", "backslashreplace"))
print(u.encode("ascii", "namereplace"))  # b'\\N{YI SYLLABLE IT}abcd\\u07b4'


u = chr(233) + chr(0x0BF2) + chr(3972) + chr(6000) + chr(13231)

for i, c in enumerate(u):
    print(i, "%04x" % ord(c), unicodedata.category(c), end=" ")
    print(unicodedata.name(c))

# Get numeric value of second character
print(unicodedata.numeric(u[1]))

# Additional Ref: https://mortoray.com/2013/11/27/the-string-type-is-broken/
