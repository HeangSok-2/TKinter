# Acknowledgement: Dr John (codemy.com)
from tkinter import *
from tkinter import messagebox  # for this function it is important to call it again like this; sepcify its name.

root = Tk()
# root.resizable(0,0)
root.title("Testing a message box")


def message():
    my_message = messagebox.askquestion("This is a message box", "Hello World!")
    Label(root, text=my_message).pack()
    # you can play around with these fields: showinfo, showwarning, showerror, askquestion (it returns string: yes, no)
    # askokcancel (it returns string: ok, cancel), askyesno (it returns int: 1, 0)

    # note: for macbigsur, whenever you use a popup message box, it will give you an error message. the problem occurs
    # to other programming languages and software as well. Example:
    # Warning: Expected min height of view: (<NSButton: 0x7fa6976208b0>) to be less than or equal to 30 but got a
    # height of 32.000000. This error will be logged once per view in violation.


my_button = Button(root, text="Click me to see a message!", command=message).pack()

root.mainloop()