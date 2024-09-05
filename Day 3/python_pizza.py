print("\nWelcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? ( S, M or L ) -- R: ")
pepperoni = input("Do you want pepperoni on your pizza? ( Y or N ) -- R: ")
extra_cheese = input("Do you want extra cheese? ( Y or N ) -- R: ")

price_small = 15
price_medium = 20
price_large = 25
price_small_pepperoni = 2
price_bigger_pepperoni = 3
price_extra_cheese = 1

total = 0

if extra_cheese == 'Y':
    total += price_extra_cheese

if size == 'S':
    total += price_small
    
    if pepperoni == 'Y':
        total += price_small_pepperoni      

elif size == 'M':
    total += price_medium
    if pepperoni == 'Y':
        total += price_bigger_pepperoni  

else:
    total += price_large
    if pepperoni == 'Y':
        total += price_bigger_pepperoni  

print(f"Your total bill will be ${total}" )