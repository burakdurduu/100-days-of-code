from tkinter import *

window = Tk()
window.config(padx=20, pady=20)
window.title("Mile to Km Converter")
is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

miles_entry = Entry()
miles_entry.config(width=10)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label()
km_label.config(width=10)
km_label.grid(row=1, column=1)

km_label2 = Label(text="Km")
km_label2.grid(row=1, column=2)


def button_clicked():
    miles = float(miles_entry.get())
    result = miles * 1.609
    km_label.config(text=round(result))


button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)
window.mainloop()
