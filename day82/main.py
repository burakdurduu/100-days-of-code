from data import MORSE_CODE_DICT, LOGO


def text_to_morse(text):
    morse_code_list = []
    for char in text:
        try:
            morse_code_list.append(MORSE_CODE_DICT[char])
        except KeyError:
            morse_code_list.append('#')
    result = " ".join(morse_code_list)
    return result


def morse_to_text(morse_code):
    text_list = []
    for char in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if char == value:
                text_list.append(key.lower())
            elif char == "   ":
                text_list.append(" ")
    result = "".join(text_list)
    return result


def main():
    print(LOGO)
    while True:
        choice = input("Choose an option:\n"
                       "1. Text to Morse Code\n"
                       "2. Morse Code to Text\n"
                       "3. Exit\n"
                       "Enter choice (1, 2, 3): ")
        if choice == "1":
            text = input("Enter Text: \n").upper()
            morse_code = text_to_morse(text)
            print(f"Morse Code:\n{morse_code}\n")
        elif choice == "2":
            morse_code = input("Enter Morse Code: \n").split(" ")
            text = morse_to_text(morse_code)
            print(f"Text:\n{text}\n")
        elif choice == "3":
            break
        else:
            print(f"{75 * '-'}\nInvalid number. Try again!\n")


if __name__ == '__main__':
    main()
