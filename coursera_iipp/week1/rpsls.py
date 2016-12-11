#! /usr/bin/python

# Assignment: Mini-project 1; Rock, paper, scissors, lizard, spock
# Author: Andrew Ludwar
# Due date: April 27, 2013; 11:00 PM MST
# Date: April 21, 2013

import random

def number_to_name(number):
    """Convert numbers to names"""
    if number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "Spock"
        return name
    elif number == 2:
        name = "paper"
        return name
    elif number == 3:
        name = "lizard"
        return name
    elif number == 4:
        name = "scissors"
        return name
    else:
        return "Error!  Didn't recognize the number provided."
    
    
def name_to_number(name):
    """Convert names to numbers"""
    if name == "rock":
        number = 0
        return number
    elif name == "Spock":
        number = 1
        return number
    elif name == "paper":
        number = 2
        return number
    elif name == "lizard":
        number = 3
        return number
    elif name == "scissors":
        number = 4
        return number
    else:
        return "Error!  Didn't recognize the name provided."
    

def rpsls(name): 
    """The main function of RPSLS game.  Compare player entry with randomly
    generated computer entry.  Display results with proper name to number
    translations """
    
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 4)
        
    result = (player_number - comp_number) % 5
        
    # if player/comp comparison is 3 or 4, player loses
    # if player/comp comparison is 1 or 2, player wins
    # if player/comp comparison is 0, it's a tie
    if (result == 1 or result == 2):
        print "Player chooses", number_to_name(player_number)
        print "Computer chooses", number_to_name(comp_number)
        print "Player wins!"
        print ""
    elif (result == 3 or result == 4):
        print "Player chooses", number_to_name(player_number)
        print "Computer chooses", number_to_name(comp_number)
        print "Computer wins!"
        print ""
    else:
        print "Player chooses", number_to_name(player_number)
        print "Computer chooses", number_to_name(comp_number)
        print "Player and computer tie!"
        print ""
    
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
