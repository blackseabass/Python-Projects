#!/usr/bin/env python

"""
File Name: week9_exercise2.py
Developer: Eduardo Garcia
Date Last Modified: 10/30/2015
Description: This program separates words that
             that are inputed by the user.
Email Address: garciaeduardo1223@gmail.com

"""

def sentenceSplitter(sentence):
    result = ''
    for i, x in enumerate(sentence):
        if i == 0:
            result = result + x
        elif x.isupper() == False:
            result = result + x
        else:
            result = result + ' ' + x.lower()
    return(result)

def main():
    my_string = input('Enter a sentence: ')
    print(sentenceSplitter(my_string))

main()
