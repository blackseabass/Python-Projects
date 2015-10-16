#!/usr/bin/env python

"""
File Name: week6_exercise3-2.py
Developer: Eduardo Garcia
Date Last Modified: 10/10/2014
Description: Program reads the golf.txt file.
Email Address: garciaeduardo1223@gmail.com

"""

def main():
    inGolf = open('golf.txt', 'r')
    names = []
    scores = []
    for line in inGolf:
        line_list = line.split(",")
        names.append(line_list[0])
        scores.append(line_list[1])

    for i in range(len(names)):
        print "{0:20}{1:10}".format(names[i], scores[i])

    inGolf.close()
