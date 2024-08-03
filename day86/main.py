from tkinter import *
import random


class TypingSpeedTest(Tk):

    def __init__(self):
        super().__init__()
        width = 800
        height = 350
        x = int((self.winfo_screenwidth() / 2) - (width / 2))
        y = int((self.winfo_screenheight() / 2) - (height / 2))
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.title("Typing Speed Test")
        self.config(bg="black", padx=5, pady=5)

        self.timer = None
        self.wpm = 0
        self.cpm = 0
        self.mistakes = 0
        self.uncorrected_words = 0
        self.current_word = ""
        self.entry = ""
        self.text = ""
        self.entry_index = 0
        self.text_index = 0
        self.list_index = 0
        self.entry_words_list = []
        self.text_list = []

        self.entry_box = Entry(fg="white", bg="black", font=("Tahoma", 50))
        self.entry_box.grid(row=2, column=0, columnspan=2, sticky=EW)
        self.entry_box.config(state=DISABLED, fg="black", bg="grey")

        self.textbox = Text(height=3, width=27, padx=10, pady=10, fg="white", bg="black", font=("Tahoma", 50))
        self.textbox.grid(row=1, column=0, columnspan=2)
        self.textbox.insert(1.0, "Welcome\nTyping Speed Test App\nPress Start Button")
        self.textbox.config(state=DISABLED, wrap=WORD)
        self.textbox.tag_config("green", foreground="green")
        self.textbox.tag_config("red", foreground="red")

        self.time_label = Label(text=f"TIME: 00", fg="yellow", bg="black", font=("Tahoma", 12))
        self.time_label.grid(row=0, column=0, sticky=W)

        self.cpm_label = Label(text=f"CPM: {self.cpm}", fg="lightgreen", bg="black", font=("Tahoma", 12))
        self.cpm_label.grid(row=0, column=0, sticky=N)

        self.wpm_label = Label(text=f"WPM: {self.wpm}", fg="cyan", bg="black", font=("Tahoma", 12))
        self.wpm_label.grid(row=0, column=0, sticky=E)

        self.mistakes_label = Label(text=f"MISTAKES: {self.mistakes}", fg="white", bg="black", font=("Tahoma", 12))
        self.mistakes_label.grid(row=0, column=1, sticky=N)

        self.start_button = Button(text="Start", command=self.start, fg="black", bg="black", font=("Tahoma", 12))
        self.start_button.grid(row=3, column=0, sticky=W)

        self.reset_button = Button(text="Reset", command=self.reset, fg="black", bg="black", font=("Tahoma", 12))
        self.reset_button.grid(row=0, column=1, sticky=SE)

    def count_down(self, count):
        if count > 0 and self.timer:
            self.timer = self.after(1000, self.count_down, count - 1)
            self.time_label.config(text=f"TIME: {count:02}", fg="yellow")
        else:
            self.time_label.config(text="TIME: 00", fg="orange")
        if count == 0:
            self.mistakes_label.config(fg="red")
            self.show_results()

    def get_words(self):
        self.clear_textbox()
        with open("words.txt") as file:
            words = file.read().split()
            self.text = " ".join(random.choice(words) for _ in range(8))
            self.textbox.config(state=NORMAL)
            self.textbox.insert(1.0, self.text)
            self.textbox.config(state=DISABLED)
            self.text_list = self.text.split(" ")

    def compare_chars(self, event):
        special_keys = ["Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R", "Meta_L", "Meta_R",
                        "Command", "Option_L", "Option_R", "Caps_Lock", "Escape", "Tab", "Return", "Delete"]
        if event.keysym in special_keys:
            return

        self.entry = self.entry_box.get()
        self.current_word = self.text_list[self.list_index]
        if len(self.entry) <= len(self.current_word):
            if self.text[self.text_index] == self.entry[self.entry_index]:
                self.textbox.tag_add("green", f"1.{self.text_index}")
                self.textbox.tag_remove("red", f"1.{self.text_index}")
                self.text_index += 1
                self.entry_index += 1
                self.cpm += 1
            else:
                self.textbox.tag_add("red", f"1.{self.text_index}")
                self.textbox.tag_remove("green", f"1.{self.text_index}")
                self.text_index += 1
                self.entry_index += 1
                self.mistakes += 1
        else:
            self.mistakes += 1

        self.update_labels()

    def compare_words(self):
        if self.entry == self.current_word:
            self.wpm += 1
            self.list_index += 1
            self.entry_words_list.append(self.current_word)
            self.wpm_label.config(text=f"WPM: {self.wpm}")
        else:
            skip_index = len(self.current_word) - self.entry_index
            self.text_index += skip_index
            self.entry_words_list.append(self.current_word)
            self.list_index += 1
            self.uncorrected_words += 1

        if len(self.entry_words_list) == len(self.text_list):
            self.get_words()
            self.entry_words_list = []
            self.list_index = 0
            self.text_index = -1

    def backspace(self, event):
        if self.entry_index != 0:
            if len(self.entry) <= len(self.current_word):
                self.entry_index -= 1
                self.text_index -= 1
                self.textbox.tag_remove("red", f"1.{self.text_index}")
                self.textbox.tag_remove("green", f"1.{self.text_index}")
                if self.text[self.text_index] != self.entry[self.entry_index]:
                    self.mistakes -= 1
                else:
                    self.cpm -= 1
            else:
                self.mistakes -= 1

            self.update_labels()
        self.entry = self.entry_box.get()

    def space(self, event):
        if self.entry_index != 0:
            self.compare_words()
            self.text_index += 1
            self.entry_index = 0
            self.entry_box.delete(0, END)

    def clear_textbox(self):
        self.textbox.config(state=NORMAL)
        self.textbox.delete(1.0, END)
        self.textbox.config(state=DISABLED)

    def clear_entrybox(self):
        self.entry_box.config(state=NORMAL)
        self.entry_box.delete(0, END)
        self.entry_box.config(state=DISABLED)

    def update_labels(self):
        self.cpm_label.config(text=f"CPM: {self.cpm}")
        self.mistakes_label.config(text=f"MISTAKES: {self.mistakes}")

    def calculate_result(self):
        gross_wpm = self.cpm / 5
        net_wpm = gross_wpm - self.uncorrected_words
        try:
            accuracy = (self.cpm / (self.cpm + self.mistakes)) * 100
        except ZeroDivisionError:
            accuracy = 0
        return f"Gross WPM: {gross_wpm:.0f}\nNet WPM: {net_wpm:.0f}\nAccuracy: {accuracy:.0f}%"

    def show_results(self):
        self.clear_textbox()
        self.clear_entrybox()

        self.textbox.config(state=NORMAL)
        self.textbox.insert(1.0, self.calculate_result())
        self.textbox.config(state=DISABLED)

        self.entry_box.config(state=NORMAL)
        self.entry_box.insert(0, "Press Reset Button")
        self.entry_box.config(state=DISABLED)

        self.unbind("<Key>")
        self.unbind("<space>")
        self.unbind("<BackSpace>")

    def start(self):
        self.bind("<Key>", self.compare_chars)
        self.bind("<space>", self.space)
        self.bind("<BackSpace>", self.backspace)
        self.clear_entrybox()
        self.clear_textbox()
        self.start_button.config(state=DISABLED)
        self.entry_box.config(state=NORMAL)
        self.entry_box.focus()
        self.timer = True
        self.get_words()
        self.count_down(60)

    def reset(self):
        self.clear_textbox()
        self.clear_entrybox()
        self.time_label.config(text=f"TIME: 00")
        self.cpm_label.config(text="CPM: 0")
        self.wpm_label.config(text="WPM: 0")
        self.mistakes_label.config(text="MISTAKES: 0", fg="white")

        self.start_button.config(state=NORMAL)
        self.entry_box.config(state=NORMAL)
        self.entry_box.insert(0, "Press Start Button")
        self.entry_box.config(state=DISABLED)

        self.textbox.config(state=NORMAL)
        self.textbox.insert(1.0, "Typing Speed Test")
        self.textbox.config(state=DISABLED)

        self.timer = None
        self.wpm = 0
        self.cpm = 0
        self.mistakes = 0
        self.uncorrected_words = 0
        self.entry = ""
        self.current_word = ""
        self.text = ""
        self.text_index = 0
        self.entry_index = 0
        self.list_index = 0
        self.entry_words_list = []
        self.text_list = []

        self.unbind("<Key>")
        self.unbind("<space>")
        self.unbind("<BackSpace>")


if __name__ == "__main__":
    app = TypingSpeedTest()
    app.mainloop()
