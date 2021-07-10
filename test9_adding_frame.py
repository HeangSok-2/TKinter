# Acknowledgement: Dr John (codemy.com)
from tkinter import *

root = Tk()
root.title("Testing on frame widget")

# put a frame into the root (window or screen)
frame = LabelFrame(root, text="This is a frame with two buttons", padx=5, pady=5)    # we use the pad here to set-
# the padding inside the frame
frame.pack(padx=10,pady=10)     # we use the pad here to set the padding outside the frame

# we can use grid inside the frame
button1 = Button(frame, text="Button 1")    # as you can see, we use frame instead of root in the parentheses
button1.grid(row=0, column=0, pady=5)
button2 = Button(frame, text="Button 2")
button2.grid(row=1, column=0, pady=5)

root.mainloop()