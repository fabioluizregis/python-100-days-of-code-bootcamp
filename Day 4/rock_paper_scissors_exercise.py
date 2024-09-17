import random

print("Welcome to the UTIMATE Rock, Paper, Scissors game!\n")

option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \nAnswer: "))

alternatives=["Rock","Paper","Scissors"]

gamer = alternatives[option]
computer = random.choice(alternatives)

print(f"You choose {gamer}")
print(f"Your oponent choose {computer}")

if gamer == computer:
    print("\nIt is a MATCH!")
elif gamer == "Rock" and computer == "Paper":
    print("\nYou Lose!")
elif gamer == "Rock" and computer == "Scissors":
    print("\nYou Won!")
elif gamer == "Paper" and computer == "Scissors":
    print("\nYou Lose!")
elif gamer == "Paper" and computer == "Rock":
    print("\nYou Won!")
elif gamer == "Scissors" and computer == "Paper":
    print("\nYou Won!")
else:
    print("\nYou Lose!")