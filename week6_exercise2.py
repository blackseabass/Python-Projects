#!/usr/bin/env python

"""
File Name: week6_exercise2.py
Developer: Eduardo Garcia
Date Last Modified: 10/9/2014
Description: Reads the ran_numbers.txt file and
             displays the total of the numbers.
Email Address: garciaeduardo1223@gmail.com

"""

def main():
        random_numbers = open('ran_numbers.txt', 'r')
        number = 0
        total = 0
        print("List of numbers:")
        for line in random_numbers.readlines():
              print(line)
              total = total+int(line)
              number +=1
        print("The total of the numbers = "+str(total))
        print("The number of the random numbers read from the file = "+str(number))
main()
