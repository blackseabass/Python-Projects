#!/usr/bin/env python
"""
File Name: week2_exercise1.py
Developer: Eduardo Garcia
Date Last Modified: 9/12/2014
Description: Asks user to input amount of total sales,
             program wll then display profit.
Email Address: garciaeduardo1223@gmail.com

"""

total_sales = float(input("Please enter the projected amount of the total sale: "))

profit = (total_sales * .23)

annual_profit = profit + total_sales
print ("Annual Profit is:", annual_profit)

input("Press Enter to exit program.")
