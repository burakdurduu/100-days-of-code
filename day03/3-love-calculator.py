# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# 🚨 Don't change the code above 👆

# Write your code below this line 👇

names = name1.lower() + name2.lower()

true_count = 0

if names.count("t"):
    true_count += names.count("t")
if names.count("r"):
    true_count += names.count("r")
if names.count("u"):
    true_count += names.count("u")
if names.count("e"):
    true_count += names.count("e")

love_count = 0

if names.count("l"):
    love_count += names.count("l")
if names.count("o"):
    love_count += names.count("o")
if names.count("v"):
    love_count += names.count("v")
if names.count("e"):
    love_count += names.count("e")

count = str(true_count) + str(love_count)
count = int(count)


if count < 10 or count > 90:
    print(f"Your score is {count}, you go together like coke and mentos.")
elif count >= 40 and count <= 50:
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}.")

# -------------------------------------------------------------

# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
#
# score = int(str(first_digit) + str(second_digit))
#
# if (score < 10) or (score > 90):
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")
