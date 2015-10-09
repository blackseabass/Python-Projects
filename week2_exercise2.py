#!/usr/bin/env python
"""
File Name: week2_exercise2.py
Developer: Eduardo Garcia
Date Last Modified: 9/12/2014
Description: Asks user to input degree in celsius to
             convert to fahrenheit.
Email Address: garciaeduardo1223@gmail.com

"""

celsius = int(input("Enter a temperature in Celsius: "))

fahrenheit = 9.0/5.0 * celsius + 32

print ("Temperature:", celsius, "Celsius = ", fahrenheit, "F")

input("Press Enter to exit program.")
