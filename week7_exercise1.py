#!/usr/bin/env python

"""
File Name: week7_exercise1.py
Developer: Eduardo Garcia
Date Last Modified: 10/15/2014
Description: Program stores and displays the numbers
             the user input. Also displays the quantity, 
             the average and the numbers ranging from
             highest to lowest.
Email Address: garciaeduardo1223@gmail.com

"""

def main():
    numbers = get_values()
    get_analysis(numbers)
    
def get_values():
    print('Please Enter A Series Of 20 Random Numbers')
    values =[]    
    for i in range(20):
        value =(int(input("Enter A Random Number " + str(i + 1) + ": ")))
        values.append(value)
               
    return values

def get_analysis (numbers):
    print("The Lowest Number Is:",  str(min(numbers)))
    print("The Highest Number Is:", str(max(numbers)))
    print("The Sum The Numbers Is:", str(sum(numbers)))
    print("The Average The Numbers Is:", str(sum(numbers)/len(numbers)))

main()
