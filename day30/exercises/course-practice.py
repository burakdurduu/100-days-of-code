# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sauhduasdsadj"])
except FileNotFoundError:
    file = open("a_file", "w")
    file.write("asjbdhshka")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
