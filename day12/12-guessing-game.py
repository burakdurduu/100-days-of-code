import random
print("Welcome to the Number Guessing Game!")
game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(1, 100)

if game_level == "hard":
    attemps = 5
else:
    attemps = 10


def play():
    global attemps
    while attemps != 0:
        guess = int(input("Mage a guess: "))
        if guess > number:
            print("Go down!")
            attemps -= 1
            print(f"You have {attemps} attemps remaining to guess the number")
        elif guess < number:
            print("Go up.")
            attemps -= 1
            print(f"You have {attemps} attemps remaining to guess the number")
        else:
            print(f"You got it answer was {number}.")
            attemps = 0
    if attemps == 0:
        print("Game Over!")


play()
