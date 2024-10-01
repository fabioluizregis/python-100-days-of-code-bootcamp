import random

word_list = ["aardvark", "babbon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")

    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")