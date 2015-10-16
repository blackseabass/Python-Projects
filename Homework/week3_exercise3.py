#!/usr/bin/env python

"""
File Name: week3_exercise3.py
Developer: Eduardo Garcia
Date Last Modified: 9/19/2014
Description: Asks the user to input number of
             seconds. The program will then display
             Days, Hours and Minutes.
Email Address: garciaeduardo1223@gmail.com

"""

minute = 60
hour = 3600
day = 86400

secs = int(input("Please enter a number of seconds: "))
ins_day = secs / day
ins_hour = secs / hour
ins_minute = secs/ minute

print("Days ", ins_day, "Hours ", ins_hour, "Minutes ", ins_minute)
