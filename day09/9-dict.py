programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again."
}
 
# retrieving Items from Dictionary
print(programming_dictionary["Bug"])
 
# adding new Items to Dictionary
programming_dictionary["True Love"] = "A hard thing to find"
 
# print(programming_dictionary)
 
# create an empty dictionary
an_empty_dictionary = {}
 
# wipe an entire dictionary
# programming_dictionary = {}
 
# editing a dictionary
programming_dictionary["True Love"] = "Love to our Angela Sensei"
# printing an entire dictionary
# print(programming_dictionary)
 
# Loop through a dictionary
 
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
