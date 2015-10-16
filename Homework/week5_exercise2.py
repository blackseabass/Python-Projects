#!/usr/bin/env python

"""
File Name: week5_exercise2.py
Developer: Eduardo Garcia
Date Last Modified: 10/4/2014
Description: User plays Rock, Paper, Sciissors with
             the computer
Email Address: garciaeduardo1223@gmail.com

"""
import random


def main():
    print("Rock. Paper. Scissors." "\n" "Enter 1 for Rock, 2 for Paper or 3 for Scissors.", "\n")
    answer()

def random_integer():
    return random.randrange(1,3)

def answer():
    player = int(input("Enter your choice: "))
    while player != 1 and player != 2 and player != 3:
        print("Invalid entry. Please try again.")
        player = int(input("Enter 1, 2, or 3.: "))
    display_answer(player)

def display_answer(player):
    computer_answer = random_integer()
    print("Computer picks: ", computer_answer, "\n")
    winner(computer_answer, player)

def winner(computer, player):
    if computer == player:
        print("Draw. Try again.")
        answer()
    elif computer == 1 and player == 2:
        print("Paper covers rock. Player wins!")
    elif computer == 1 and player == 3:
        print("Rock smashes scissors. Computer wins.")
    elif computer == 2 and player == 1:
        print("Paper covers rock. Computer wins.")
    elif computer == 2 and player == 3:
        print("Scissors cut paper. Player wins!")
    elif computer == 3 and player == 1:
        print("Rock smashes scissors. Player wins!")
    elif computer == 3 and player == 2:
        print("Scissors cut paper. Computer wins.")
        
main()
