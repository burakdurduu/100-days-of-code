# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"    A     B     C\n1 {row1}\n2 {row2}\n3 {row3}")
position = input("Where do you want to put the treasure? e.g. 'A1', 'B3', 'C2'\n>")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# Write your code above this row 👆
if position[0].isdigit():
    columns = int(position[0]) - 1
    rows = int(position[1]) - 1
    map[rows][columns] = "X"
else:
    letter = position[0].lower()
    letters = ["a", "b", "c"]
    letter_index = letters.index(letter)
    number_index = int(position[1]) - 1
    map[number_index][letter_index] = "X "

# 🚨 Don't change the code below 👇
print(f"    A     B     C\n1 {row1}\n2 {row2}\n3 {row3}")