# Day 1 - consists in learning printing, commenting, debugging, string manipulation and variables.

print("Hello, Fabio!")

# Printing a recipe
print("")
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
print("")

# Breaking lines while single printing
print("Line 1 \nLine 2 \nLine 3")
print("")

# Concatenating Strings
print("Hello," + " Fabio!")
print("")

# Capturing keyboard entrances
print("Hello, " + input("What is your name? ") + "!")

# Using Variables
name = input("What is your name? ")
print(name)

# Printing the number of chars in a word
print(len(input("Type a word to count chars: ")))

# Day1 Project: Band Name Generator

print("\nWelcome to the Band Name Generator.")
name_of_the_city_grown = input("What's the nameof the city you grew up in?\n R: ")
name_of_your_pet = input("\nWhat's your pet name?\n R: ")

print("\n\nYou band name could be " + name_of_the_city_grown + " " + name_of_your_pet)