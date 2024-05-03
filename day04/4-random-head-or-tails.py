import random

flip = random.randint(0, 100)

if flip >= 0 and flip < 50:
    print("Heads")
else:
    print("Tails")
