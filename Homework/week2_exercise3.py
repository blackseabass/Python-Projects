#!/usr/bin/env python
"""
File Name: week2_exercise3.py
Developer: Eduardo Garcia
Date Last Modified: 9/12/2014
Description: Asks user to input number of cookies
             to make. The script will then dispay
             the number of ingredients needed.
Email Address: garciaeduardo1223@gmail.com

"""

amount = int(input("Please enter the amount of cookies you would like to make: "))

sugar = 1.5
butter = 1
flour = 2.75


new_sugar = sugar * (48 / amount)
new_butter = butter * (48 / amount)
new_flour = flour * (48 / amount)


print ("Cups of sugar needed: ", format(new_sugar, '.2f'))
print ("Cups of butter needed: ", format(new_butter, '.2f'))
print ("Cups of flour needed: ", format(new_flour, '.2f'))

input("Press Enter to exit program.")
