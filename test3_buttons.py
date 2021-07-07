from tkinter import *

root = Tk()


def my_click():
    my_label = Label(root, text="Hello Meow!")
    my_label.pack()


my_button = Button(root, text="Click Me!", command=my_click, fg="blue")
my_button.pack()

root.mainloop()



