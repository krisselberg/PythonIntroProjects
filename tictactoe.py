# Tic Tac Toe
import random

# Create options for player and computer
options = ["Rock", "Paper", "Scissors"]

# Prints results of match with computer
def match(val2):
    val1 = options[random.randint(0,2)]
    if val1 == val2: 
        print("Draw.")
    elif val1 == "Rock":
        if val2 == "Paper":
            print("You won! Your paper COVERED the rock.")
        elif val2 == "Scissors":
            print("You lost! Your scissors got SMASHED by the rock.")
    elif val1 == "Paper":
        if val2 == "Rock":
            print("You lost! Your rock got COVERED by the paper.")
        if val2 == "Scissors":
            print("You won! Your scissors CUT through the paper.")
    else:
        if val2 == "Paper":
            print("You lost! Your paper got CUT by the scissors.")
        if val2 == "Rock":
            print("You won! Your rock SMASHED the scissors.")

# Plays multiple rounds with computer in the command line
playing = True
while (playing == True):
    play = input("Want to play tic tac toe (y/n)?")
    if play == "y":
        val2 = input("Rock, Paper, or Scissors?")
        match(val2)
    elif play == "n":
        print("Have a great day/night!")
        playing = False
    else:
        print("That is not a valid input. Try again.")
