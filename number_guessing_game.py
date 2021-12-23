# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 305.
# Q. 20 Number Guessing Game.

from random import *
from matplotlib.pyplot import *

MIN = 1
MAX = 100

m = 1
x_values = []


print("--- NUMBER GUESSING GAME ---\n")
print("Enter Number Between 1 - 100.")

while m == 1:
    x = randint(MIN, MAX)
    x0 = int(input("Enter Guess Number: x0 = "))

    if x0 >= MIN and x0 <= MAX:
        x_values.append(x0)

        if x > x0:
            print("Too Low Try Again...")

        elif x < x0:
            print("Too High Try Again...")

        else:
            print("Congartulations!")

            N = len(x_values)
            if N <= 3:
                print("Great Guess!")
            print("Number of Times Guessed: N = ", N)
            print("Correct Guess: x = ", x0)
            title("Statistics.")
            xlabel("Number of Attempts.")
            ylabel("Guessed Numbers.")
            hist(x_values, bins = N, ec = "black")
            show()

            print("\n Press 1 To Start Again...")
            m = int(input())
    
    else:
        print("Error!")
        print("Enter Number Between 1 - 100.")
