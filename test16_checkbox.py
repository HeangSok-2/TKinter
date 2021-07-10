# acknowledgement = bro code (youtube.com)

from tkinter import *


def display():
    if x.get() == 1:
        label =Label(window, text=x.get()).pack()
    else:
        label = Label(window, text=x.get()).pack()


window = Tk()

x = IntVar()

checkbox = Checkbutton(window, text="python", variable=x, onvalue=1, offvalue=0, command=display,)
checkbox.pack()
checkbox.config(font=("Arial", 20)) # changes the font
checkbox.config(fg="#0000FF") # foreground color
# checkbox.config(bg="#000000") # background color
# checkbox.config(activeforeground="#0000FF") # make the screen doesn't blink when you click
# checkbox.config(activebackground="#000000") # make the screen doesn't blink when you click; test the code yourself
photo = PhotoImage(file='AppBreweryWallpaper 1.png')
checkbox.config(image=photo, compound='left')
checkbox.config(padx=25, pady=10, width=250, height=50)
checkbox.config(selectcolor='green')

window.mainloop()