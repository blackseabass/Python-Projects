#!/usr/bin/env python

"""
File Name: week7_exercise2.py
Developer: Eduardo Garcia
Date Last Modified: 10/15/2014
Description: The program reads the answers key and
			 compares the user's input. Then the 
			 program calculates the number of right
			 and wrong ansewrs and display the amount
			 right and the amount wrong.
Email Address: garciaeduardo1223@gmail.com

"""

def main( ): 
    key = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 
        'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
    student_answers = read_student('student_answers.txt')
    pass_fail(key, student_answers)


def read_student(path):
    with open(path, 'r') as infile:
        contents = infile.read()

    # Automatically gets rid of the newlines.
    return contents.split('\n') 

def pass_fail(answers, student):
    correct_list = []
    wrong_list = []

    # Use the 'enumerate' function to return the index.
    for index, (ai, bi) in enumerate(zip(answers, student)):
        # since problems start with 1, not 0
        problem_number = index + 1 

        if ai == bi:
            correct_list.append(problem_number)
        else:
            wrong_list.append(problem_number)

    # Print the length of the list, not the list itself.
    print(len(correct_list), 'were answered correctly')
    print(len(wrong_list), 'questions were missed')

    if len(correct_list) >= 15:
        print('Congrats, you have passed')
    else: 
        print('Sorry, you have failed. Please study and try again in 90 days')
        print('Any attempt to retake test before 90 days will result in suspension of any licenses')

    # Display each missed number on a separate line
    print ('You missed questions numbers:')
    for num in wrong_list:
        print('    ' + str(num))
  
main()
