import random

letters = ['a','b','c','d','e','f','g','h','j','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print('Welcome to the PyPasswordGenerator!')
nr_letters = int(input(f"How many letters would you like in your password?\nAnswer: "))
nr_symbols = int(input(f"How many symbols would you like?\nAnswer: "))
nr_numbers = int(input(f"How many numbers would you like?\nAnswer: "))

password = []

for letter in range(0, nr_letters):
    password.append(random.choice(letters))
for symbol in range(0, nr_symbols):
    password.append(random.choice(symbols))
for number in range(0,nr_numbers):
    password.append(random.choice(numbers))

print("\n\nEasy way: ")
print(*password,sep="")

scrambled_pass = []
for item in range(0, len(password)):
    scrambled_pass.append(random.choice(password))
    password.remove(scrambled_pass[item])

print("\nScrambled pass: ")
print(*scrambled_pass,sep="")

final_in_string = ""
for char in scrambled_pass:
    final_in_string += char

print(f"Your randomized password is: {final_in_string}")