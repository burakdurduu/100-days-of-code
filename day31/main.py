from tkinter import *
import pandas as pd
import random

# English - Turkish Flash Card Project.

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/english-words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Turkish", fill="white")
    canvas.itemconfig(card_word, text=current_card["Turkish"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


def is_know():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightbackground=BACKGROUND_COLOR, background=BACKGROUND_COLOR)
canvas_image = canvas.create_image(1, 1, anchor=NW, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="Title")
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"), text="word")

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=3, column=1)

check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image, highlightbackground=BACKGROUND_COLOR, command=is_know)
know_button.grid(row=3, column=0)

next_card()

window.mainloop()
