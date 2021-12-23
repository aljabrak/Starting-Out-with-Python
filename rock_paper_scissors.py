# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 306.
# Q. 21 Rock, Paper, Scissors Game.

from random import *

MIN = 1
MAX = 3
data = [1, 2, 3]
print("----- ROCK, PAPER, SCISSORS GAME. -----")
print("PRESS \n 1) Rock. \n 2) Paper. \n 3) Scissors.")

m = 1

while m == 1:
    x = randint(1,3)
    u = int(input("user = "))

    if u in data:
        if x == 1 and u == 3:
            print("Rock Smashes Scissors.")
            print("You Lost...")
            print("Enter 1 to Start Again...")
            m = int(input())
            
        elif u == 3 and x == 2:
            print("Scissors Cuts Paper.")
            print("You Won...")
            print("Enter 1 to Start Again...")
            m = int(input())

        elif u == 2 and x == 1:
            print("Paper Wraps Rock.")
            print("You Won...")
            print("Enter 1 to Start Again...")
            m = int(input())

        elif x == 3 and u == 1:
            print("Rock Smashes Scissors.")
            print("You Won...")
            print("Enter 1 to Start Again...")
            m = int(input())

        elif u == 2 and x == 3:
            print("Scissors Cuts Paper.")
            print("You Lost...")
            print("Enter 1 to Start Again...")
            m = int(input())

        elif u == 1 and x == 2:
            print("Paper Wraps Rock.")
            print("You Lost...")
            print("Enter 1 to Start Again...")
            m = int(input())

        else:
            print("Same Choice.")
            print("Enter 1 to Start Again...")
            m = int(input())

    
    else:
        print("Error!")
        print("Enter Correct Input.")
        m = 1
