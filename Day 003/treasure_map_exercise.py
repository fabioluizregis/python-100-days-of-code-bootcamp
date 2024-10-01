print("=============================================")
print("         Welcome to Treasure Island.         ")
print("    Your mission is to find the treasure.    ")
print("=============================================")
print()
print("You're on a dark cave and there are two paths")
print("that you can take!")
print("Wich one shall you choose? Left or Right?")
option = input("Type your answer (Left or Right) - Answer: ")

if option == "Right" or option == "right" or option == "RIGHT":
    print("\n\n\nArrrrgh! You felt in a hole and died!!   GAME OVER!!!")
elif option == "Left" or option == "left" or option == "left":
    print("\n\nGreat choice, lets continue our journey!")
    print("After walking for a while, you've found a great")
    print("portion of watter and don't know if it is a river or a lake")
    print("\nWhat do you want to do in this case?")
    print("Try to swim or wait to see if something like a boat appears?")
    option = input("Type your answer (Swim or Wait) - Answer: ")
    if option == "Swim" or option == "swim" or option == "SWIM":
        print("\n\n\nArrrgh! It has crocodiles in it and you died!!    GAME OVER")
    elif option == "Wait" or option == "wait" or option == "WAIT":
        print("\nThat's the best choice, this is a river infestated with crocodiles.")
        print("A boat was near to you and you crossed it safety!")

        print("\nAfter getting deeper on the cave, somehow you found three doors.")
        print("You just can choose just one of the doors, wich one shall you choose?")
        print("There is one door Red, one Yellow and a Blue one")
        option = input("Choose your door (Red, Yellow or Blue) - Answer: ")

        if option == "Red" or option == "red" or option == "RED":
            print("\n\n\nFIRE! you are burning like hell and you died!!    GAME OVER")
        elif option == "Blue" or option == "blue" or option == "BLUE":
            print("\n\n\nBEASTS everywhere, they attacked you and you died!!    GAME OVER")
        elif option == "Yellow" or option == "yellow" or option == "YELLOW":
            print("\n\n\nFound the GOLDEN ticket, you WON and is rich now! GO BUY A GOOD GAME!")
        else:
            print("The option you choose is wrongly typed or does not exist.")
    else:
        print("The option you choose is wrongly typed or does not exist.")
else:
    print("The option you choose is wrongly typed or does not exist.")