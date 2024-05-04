numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Burak"
letter_list = [letter for letter in name]
print(letter_list)

range_list = [i*2 for i in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [num*num for num in numbers]
# or
squared_numbers = [num**2 for num in numbers]

# Write your code 👆 above:

print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above
#
# # Write your 1 line code 👇 below:
#
result = [num for num in numbers if num % 2 == 0]
#
# # Write your code 👆 above:
#
print(result)

with open("file1.txt") as data1:
    data1 = data1.read()
    file1 = data1.split("\n")
    file1.pop()

with open("file2.txt") as data2:
    data2 = data2.read()
    file2 = data2.split("\n")
    file2.pop()

result = [int(num) for num in file1 if num in file2]
print(result)

# or \n readlines can be changed int dont need to split() and pop()

with open("file1.txt") as data1:
    data1 = data1.readlines()
with open("file2.txt") as data2:
    data2 = data2.readlines()

result = [int(num) for num in file1 if num in file2]
print(result)
