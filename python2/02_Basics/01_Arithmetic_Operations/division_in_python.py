"""
If x equals to an even number:
 x % 2 = 0
 If x equals to an odd number:
 x % 2 > 0
"""
 12345 % 10 = 5
 12345 % 100 = 45
 12345 % 1000 = 345
 12345 % 10000 = 2345
 12345 % 100000 = 12345

 12345 / 1 = 12345
 12345 / 10 = 1234
 12345 / 100 = 123
 12345 / 1000 = 12
 12345 / 10000 = 1

 From left to right, I want the 3rd digit...
 12345 % 1000 / 100   (this evaluates to 3)
 12345 / 100 % 10     (this evaluates to 3)

 From left to right, I want the 4th digit...
 12345 / 10 % 10      (this evaluates to 4)
 12345 % 100 / 10     (this evaluates to 4)
