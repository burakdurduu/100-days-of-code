import pandas
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    try:
        user_input = input("Enter a word: ").upper()
        result_list = [data_dict[letter] for letter in user_input]
        print(result_list)
        break
    except KeyError:
        print("Sory, only letters in the alphabet please.")
