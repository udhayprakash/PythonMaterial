"""
Purpose: Representing big(large and small) numbers

Numeric literal allow optional underscores to help
improve the readability
"""

num = 100
print("num =", num)

# Larger numbers
speed_of_light = 299792458
print(type(speed_of_light), speed_of_light)

speed_of_light = 299, 792, 458
print(type(speed_of_light), speed_of_light)

speed_of_light = 299_792_458
print(type(speed_of_light), speed_of_light)

speed_of_light = "299_792_458"
print(type(speed_of_light), speed_of_light)
print()

# smaller numbers
pi_value = 3.1415_9232_2321_3453
print(type(pi_value), pi_value)

avogadro_number = 6.022_140_857e23
print(type(avogadro_number), avogadro_number)
print()

print(1_2_3_4_53_213_213)  # 123453213213
# print(1_2_3_4_53_213__213)  # NO MORE THAN ONE CONTINOUS UNDERSCROES SyntaxError: invalid decimal literal
