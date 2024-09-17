# Randomisation and Python Lists

import random

print(random.randint(1,10)) # randomise an integer number between 1-10

print(random.random()) # generates a random float number between 0 and 1 (not including the number 1)

print(random.uniform(1, 10)) # generates random float number, including the range

heads_or_tails = random.randint(0,1)
if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
