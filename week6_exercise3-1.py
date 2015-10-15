#!/usr/bin/env python

"""
File Name: week6_exercise3-1.py
Developer: Eduardo Garcia
Date Last Modified: 10/10/2014
Description: Asks user for player names and scores.
             program then writes them to golf.txt.
Email Address: garciaeduardo1223@gmail.com

"""

def main():
    counter = 0
    outGolf = open('golf.txt', 'w')
    numPlayers = str("Please enter the number of players:")

    while counter < numPlayers:
        name = str("Please enter the player's name:")
        outGolf.write(name + ",")
        score = int("Please enter that player's score:")
        outGolf.write(str(score) + "\n")
        counter = counter + 1
    outGolf.close

main()
