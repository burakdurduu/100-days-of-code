from tkinter import *

window = Tk()
window.title("Test")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)


def button_clicked():
    my_label.config(text=input1.get())


button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)
button2 = Button(text="Dont click me")
button2.grid(row=0, column=3)
input1 = Entry(width=10)
input1.grid(row=2, column=4)

window.mainloop()
