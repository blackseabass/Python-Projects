#!/usr/bin/env python
"""
File Name: week4_exercise1.py
Developer: Eduardo Garcia
Date Last Modified: 9/26/2014
Description: Asks user for days worked, then
             calculates pay in pennies that
             double each day.
Email Address: garciaeduardo1223@gmail.com

"""

ndays = input("Enter the number of days worked: ")
pay = 0.005

for day in range(1,ndays+1):
    pay *= 2.0
    print (" Day", day, " Salary", pay)

print ("Your salary on day", ndays, "would be $%.2f" % pay)
