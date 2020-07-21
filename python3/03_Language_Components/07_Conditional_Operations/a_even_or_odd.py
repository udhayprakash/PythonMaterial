# Input from user
number = int(input("Enter a number to be tested: "))
 
# Logic: determining odd/even status using the modulus arithmetic operator
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")
