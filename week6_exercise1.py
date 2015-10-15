#!/usr/bin/env python

"""
File Name: week6_exercise1.py
Developer: Eduardo Garcia
Date Last Modified: 10/9/2014
Description: Generates random numbers based on how
             many the users asks to generates. it then
             saves the numbers to ran_number.txt.
Email Address: garciaeduardo1223@gmail.com

"""


import random

def main():
   
    random_numbers = open('ran_numbers.txt', 'w')
    
    qty_numbers =  int(input('Input how many random numbers should be written to the file: '))
    print('Your list of random numbers are: ')
   
    for count in range (qty_numbers):
        number = random.randint(1,500)
        
        print(number)
        random_numbers.write(str(number)+ '\n')
        random_numbers.close()
        
    print('Your list of random numbers have been written to the file named')
    print('ran_numbers.txt')
main()
