#!/usr/bin/env python
"""
File Name: week4_exercise2.py
Developer: Eduardo Garcia
Date Last Modified: 9/26/2014
Description: Make a conversion table between 0 and 20
             between Celsius to Fahrenheit.
Email Address: garciaeduardo1223@gmail.com

"""

start = 0
end = 21
increment = 1

print("The following table shows conversion of Celsius to Fahrenheit")
print( "between 0 and 20 degrees Celsius.")
print("")
print("Celsius\t  Fahrenheit")
print("_____________________")

for Celsius in range (start, end, increment):
    Fahrenheit = (9 / 5) * Celsius + 32
    print(Celsius, "\t", format(Fahrenheit, ".1f"))
