#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

new_letters = ""
for l in range(nr_letters):
    random_letter = random.randint(0, len(letters)-1)
    l = letters[random_letter]
    new_letters += l

new_symbols = ""
for s in range(nr_symbols):
    random_symbol = random.randint(0, len(symbols)-1)
    s = symbols[random_symbol]
    new_symbols += s

new_numbers = ""
for n in range(nr_numbers):
    random_number = random.randint(0, len(numbers)-1)
    n = numbers[random_number]
    new_numbers += n

# simple password:
password = new_letters + new_symbols + new_numbers
print(f"Here is your password : {password}")

# mixed password:
mixed_password = list(password)
random.shuffle(mixed_password)
string_mixed_password = "".join(mixed_password)
print(f"Here is your mixed password : {string_mixed_password}")

# alternative mixed password:
alternative_string = ""
for i in mixed_password:
    alternative_string += i
print(f"Here is your mixed password : {alternative_string}")
