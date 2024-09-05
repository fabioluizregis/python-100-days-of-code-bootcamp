# Conditional Statements, Logical Operators, CodeBlocks and Scope

# Rollercoaster exercise
print()

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? R: "))

if height >= 120:
    print("You can ride the rollercoaster! \\o/")
    age = int(input("How old are you? R: "))
    ticket = 0

    if age <= 12:
        print("Child thickets are $5")
        ticket = 5
    elif age <= 18:
        print("Youth tickets are 7")
        ticket = 7
    else:
        print("Adult tickets are $12")
        ticket = 12

    photo = (input("Do you want to have a photo take? Type y for YES and n for No"))

    if photo == "y":
        ticket = ticket + 3
        print(f"You have to pay {ticket}")
    else:
        print(f"You have to pay {ticket}")


else:
    print("Sorry, you have to grow taller before you can ride! =(")

print()

# Operators
# >   --> Greater Than
# >=  --> Greater Than or Equal
# <   --> Less Than
# <=  --> Less Than or Equal
# ==  --> Equal
# !=  --> Not Equal

# The Module Operator

print(10 % 3)
# It shows the remainder of an operation
# In this case, 10 / 3 is 3, so the remainder is 1


