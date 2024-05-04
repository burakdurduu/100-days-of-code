with open("./Input/Names/invited_names.txt") as file:
    names = file.read()

name_list = names.split("\n")

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    starting_letter = starting_letter.read()

    for name in name_list:
        last_text = starting_letter.replace("[name]", name)
        file_name = name
        with open(f"./Output/ReadytoSend/letter_for_{file_name}", "w") as new_file:
            new_file.write(last_text)
