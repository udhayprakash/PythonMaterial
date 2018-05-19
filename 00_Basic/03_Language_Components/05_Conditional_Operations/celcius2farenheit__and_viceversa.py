#!python -u 
"""
Purpose: changing weather from C to F OR F to C
"""

mode = str(raw_input(("enter unit in Celsius(c) or Fahrenheit(f): "))
temp = int(raw_input(("please enter the temp: "))

if mode == 'c':
    Fahrenheit = round((1.8 * temp) + 32)
    print ("Temp in *C:", temp, " = ", "Temp in *F:", Fahrenheit)
else:
    Celsius = round((temp - 32) * 5.0/9.0)
    #Celsius = (temp - 32) * 5.0/9.0
    print ("Temp in *F:", temp, " = ", "Temp in *C:", Celsius)
