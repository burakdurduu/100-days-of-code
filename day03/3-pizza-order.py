# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
""" 
Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1 """

s = 15
m = 20
l = 25
total = 0
ps = 2
pml = 3
c = 1

if size == "S":
    total += s
    if add_pepperoni == "Y":
        total += ps
    if extra_cheese == "Y":
        total += c
    print(f"Your final bill is: ${total}.")
elif size == "M":
    total += m
    if add_pepperoni == "Y":
        total += pml
    if extra_cheese == "Y":
        total += c
    print(f"Your final bill is: ${total}.")
elif size == "L":
    total += l
    if add_pepperoni == "Y":
        total += pml
    if extra_cheese == "Y":
        total += c
    print(f"Your final bill is: ${total}.")
