#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number == 0:
    print(f"{number:d} zero")
elif number > 0:
    print(f"{number:d} is positive")
else:
    print(f"{number:d} is negative")
    
