# Assignment: Mini-project 2; Guess the number
# Author: Andrew Ludwar
# Due date: May 4, 2013; 11:00 PM MST
# Date: May 3, 2013

import simplegui
import random
import math

num_range = 100
num_guesses = 7

def init():
    """ Starts the game"""
    global secret_number, num_range, num_guesses
    print "New game.  Range is from 0 to", num_range
    print "Number of remaining guesses is", num_guesses
    print ""
    secret_number = random.randrange(0, num_range)
       
def range100():
    """ Button that changes range to range [0,100) and restarts """
    global secret_number, num_range, num_guesses
    
    secret_number = random.randrange(0, 100)
    num_range = 100
    num_guesses = 7
    
    init()

def range1000():
    """ Button that changes range to range [0,1000) and restarts """
    global secret_number, num_range, num_guesses
    
    secret_number = random.randrange(0, 1000)
    num_range = 1000
    num_guesses = 10  
    
    init()
    
def get_input(guess):
    global num_guesses, secret_number
    player_guess = int(guess)
    
    print "Guess was", player_guess
    
    num_guesses = num_guesses - 1
    print "Number of remaining guesses is", num_guesses
    
    if player_guess > secret_number:
        print "Lower!"
        print ""
        if num_guesses == 0:
            print "Player loses!  Out of guesses."
            print ""
            init()
    elif player_guess < secret_number:
        print "Higher!"
        print ""
        if num_guesses == 0:
            print "Player loses!  Out of guesses."
            print ""
            init()
    elif player_guess == secret_number:
        print "Correct! Player wins!"
        print ""
        init()
                

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100]", range100, 200)
frame.add_button("Range is [0, 1000]", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

init()

# start frame
frame.start()
