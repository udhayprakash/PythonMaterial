#!/usr/bin/python3
"""
Purpose: New-Style String formatting
"""
import math

print("" % ())  # OLD Style
print("{}".format(""))  # New Style

print("{}".format("udhay"))  # 'udhay'
print("{{}}".format("udhay"))  # '{}'
print("{{{}}}".format("udhay"))  # '{udhay}'
print()

print("{} and {}".format("cat", "mouse"))
print("{} and {}".format(213, "mouse"))
print("{} and {}".format(213.0, True))
print("{} and {}".format(None, True))
print()

print("{} and {}".format(None, True))
print("{0} and {1}".format(None, True))
print("{1} and {0}".format(None, True))
print()

# print('{} and {}'.format(None))
# IndexError: Replacement index 1 out of range
# for positional args tuple

print("{0} and {0}".format(None))
print()


print("{}".format(1234567890.88))  # 1234567890.88
print("{:}".format(1234567890.88))  # 1234567890.88
print("{:,}".format(1234567890.88))  # 1,234,567,890.88
print("{:_}".format(1234567890.88))  # 1_234_567_890.88
print("{:-}".format(1234567890.88))  # 1234567890.88
print("{:+}".format(1234567890.88))  # +1234567890.88
print("{:+}".format(-1234567890.88))  # -1234567890.88
print()

# similar to str.zfill()
print("{:=10}".format(12348))  #      12348
print("{:0=10}".format(12348))  # 0000012348
print("{:a=10}".format(12348))  # aaaaa12348
print()

# Alignment
print("{:<20}".format("left aligned"))  # 'left aligned        '
print("{:>20}".format("right aligned"))  # '       right aligned'
print("{:^20}".format("centered"))  # '      centered      '
# with fill character
print("{:-^20}".format("centered"))  # '------centered------'
print("{:*^20}".format("centered"))  # '******centered******'
print()

# formatting
print("{}".format(1024), 1024)  # 1024 1024
print("{:b}".format(1024), bin(1024))  # 10000000000 0b1000000000
print("{:o}".format(1024), oct(1024))  # 2000 0o2000
print("{:x}".format(1024), hex(1024))  # 400 0x400
"""
>>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
>>> # with 0x, 0o, or 0b as prefix:
>>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'
"""
print()


print("math.pi", math.pi)  # 3.141592653589793
print("{}".format(math.pi))  # 3.141592653589793
# print('{:d}'.format(math.pi))
print("{:f}".format(math.pi))  # 3.141593
print("{:F}".format(math.pi))  # 3.141593
print("{:g}".format(math.pi))  # 3.14159
print()

print("{:f}".format(math.pi))  # 3.141593
print("{:9f}".format(math.pi))  # 3.141593
print("{:9.3f}".format(math.pi))  #    3.142
print()

# To multiply number with 100 and show % in result
print("{:%}".format(math.pi))  # 314.159265%
print("{:%}".format(7))  # 700.000000%
print()

print("Name:{} Age:{} Salary:{}".format("udhay", 99, 9999.9999))
print(
    """
        Name  :{}
        Age   :{}
        Salary:{}""".format(
        "udhay", 99, 9999.9999
    )
)

print(
    """
        Name  :{0}
        Age   :{1}
        Salary:{2}""".format(
        "udhay", 99, 9999.9999
    )
)
#                               0      1     2

print(
    """
        Name  :{0} Name  :{0} Salary:{2}
        Age   :{1} Name  :{0}
        Salary:{2}""".format(
        "udhay", 99, 9999.9999
    )
)
#                               0      1     2


print(
    """
        Name  :{1} Name  :{1} Salary:{1}
        Age   :{1} Name  :{1}
        Salary:{1}""".format(
        "udhay", 99, 9999.9999
    )
)
#                               0      1     2

print(
    """
        Name  :{NAME} Name  :{NAME} Salary:{SALARY}
        Age   :{AGE} Name  :{NAME}
        Salary:{SALARY}""".format(
        NAME="udhay", AGE=99, SALARY=9999.9999
    )
)
# print(NAME) # NameError: name 'NAME' is not defined

# ------------------------------------------------------------
# Method 1
print(
    """
        Dear {customer},
                Your account ending with {accound_last_4_digits} was
                deducted {transaction_amount} on {transaction_time}.

        Thank you for shopping. Visit again!!!
         """.format(
        customer="Vijay Malya",
        accound_last_4_digits=1134,
        transaction_amount="20.5 crores",
        transaction_time="12th June 1947 12:34:45",
    )
)
# Method 2
result = {
    "customer": "Vijay Malya",
    "accound_last_4_digits": 1134,
    "transaction_amount": "20.5 crores",
    "transaction_time": "12th June 1947 12:34:45",
}

print(
    """
        Dear {customer},
                Your account ending with {accound_last_4_digits} was
                deducted {transaction_amount} on {transaction_time}.

        Thank you for shopping. Visit again!
         """.format(
        **result  # dictionary unpacking
    )
)
# mydict = {'a': 1, 'b': 2} => **mydict ==>  a =1, b=2

# Method 3
print(
    """
        Dear {customer},
                Your account ending with {accound_last_4_digits} was
                deducted {transaction_amount} on {transaction_time}.

        Thank you for shopping. Visit again!
         """.format_map(
        result
    )
)
