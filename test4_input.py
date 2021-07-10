# Acknowledgement: Dr John (codemy.com)
from tkinter import *

root = Tk()

# create input

labal1 = Label(root,text="Enter your firstname: ").grid(row=0, column=0)
entry1 = Entry(root, width=25)
entry1.grid(row=0, column=1)

labal2 = Label(root,text="Enter your firstname: ").grid(row=1, column=0)
entry2 = Entry(root,width=25)
entry2.grid(row=1, column=1)


def click_me():
    my_label = Label(root, text=f"hello {entry1.get()} {entry2.get()} !") # .get() is used to retrieve values from input
    my_label.grid(column=1, sticky=W) # sticky is used to set the alignment; W means West or left

# create button 

button = Button(root, text="Click me!", command=click_me, fg="blue").grid(row=2, column=0, sticky=E) # E means East


root.mainloop()