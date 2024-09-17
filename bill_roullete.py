import random

print("Who will pay the bill?\n")

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st option
print(f"{random.choice(friends)} will pay the bill at this time!!")


# 2nd option
roullete = random.randint(0,len(friends))

print(f"{friends[roullete]} will pay the bill at this time!!")