#!/usr/bin/env python

"""
File Name: week3_exercise1.py
Developer: Eduardo Garcia
Date Last Modified: 9/19/2014
Description: Asks user to input number 1-7 then
             displays the corresponding day.
Email Address: garciaeduardo1223@gmail.com

"""

day = int(input("Please enter a number of 1-7: "))

if day == 1:
    print ("It is Monday.")
if day == 2:
    print ("It is Tuesday.")
if day == 3:
    print ("It is Wednesday.")
if day == 4:
    print ("It is Thursday.")
if day == 5:
    print ("It is Friday.")
if day == 6:
    print ("It is Saturday.")
if day == 7:
    print ("It is Sunday.")
else:
    print ("Invalid Number.")
