from tkinter import *


def message():
        label = Label(window, text=f"Today is {var.get()}").pack()


window = Tk()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

var = StringVar()
var.set(options[0])

drop_box= OptionMenu(window, var, *options) # for the list, we need to put * in the front. var is the variable.
drop_box.pack(padx=30, pady=5)

button = Button(window, text="Click Here!", command=message).pack(pady=5)



window.mainloop()