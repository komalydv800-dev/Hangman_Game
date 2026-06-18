import random

words = ["python", "computer", "coding", "program", "developer"]

word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Guess a letter: ")

    if guess in guessed_letters:
        print("You already guessed this letter")

    elif guess in word:
        guessed_letters.append(guess)
        print("Correct!")

    else:
        attempts -= 1
        guessed_letters.append(guess)
        print("Wrong guess!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("You lost! The word was:", word)
