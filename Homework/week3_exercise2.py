#!/usr/bin/env python

"""
File Name: week3_exercise2.py
Developer: Eduardo Garcia
Date Last Modified: 9/19/2014
Description: Asks the user to input number of
             packages purchased. Then display
             the value of discount and total amount.
Email Address: garciaeduardo1223@gmail.com

"""

number_of_packages_purchased = float(input ('Enter value of number of packages purchased: '))

total_amount = number_of_packages_purchased * 99
discount = 0

if number_of_packages_purchased >= 10:
    discount = total_amount * 0.1
if number_of_packages_purchased >= 20:
    discount = total_amount * 0.2
if number_of_packages_purchased >= 50:
    discount = total_amount * 0.3
if number_of_packages_purchased >= 100:
    discount = total_amount * 0.4
total_amount = total_amount-discount
print ('Value of discount: ' + repr (discount))
print ('Value of total amount: ' + repr (total_amount))
