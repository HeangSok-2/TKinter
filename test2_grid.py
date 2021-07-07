from tkinter import *

root = Tk()

# creating label

my_label1 = Label(root,text="Hello world!")
my_label2 = Label(root,text="My name is meow.")

# shoving it onto the screen

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=5)

# keep showing the screen, always use it at the end of your code

root.mainloop()
