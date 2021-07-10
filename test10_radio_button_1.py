# Acknowledgement: Bro code (youtube.com)
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from os import *

window = Tk()
# window.geometry("250x125")


def choice():
    for y in range(3):
        if x.get() == y:
            my_label = Label(window,text=landscape[y])
            my_label.pack()


landscape = ["Landscape 1", "Landscape 2", "Landscape 3"]
img_list = []
for img in listdir("./Wallpapers/jpg wallpapers"):  #loops through directory
    i = Image.open(f"./Wallpapers/jpg wallpapers/{img}")    #open images first
    i.thumbnail((30, 30))     #change images size
    j = ImageTk.PhotoImage(i)   #need to use this funtion, or tkinter won't recognise the images
    img_list.append(j)

x = IntVar()

for index in range(len(landscape)):
    radiobuttons = Radiobutton(window,
                              text=landscape[index], # adds text to radio button
                              variable=x, # group radiobuttons together if they share the same variable
                              value=index, # assigns each radio button a different value
                              padx=25, # add padding on x-axis
                              font=("Arial", 25), # set a font
                              image= img_list[index], # adds image to radio button
                              compound= 'left', # show both image (left-side) and text
                              indicatoron=0, # eliminate circle indicators
                              width=375, # set width of button
                              command=choice # set a function
                              )
    radiobuttons.pack(anchor=W, fill=tkinter.BOTH)

label = Label(window, text= "please select one landscape!", bd=1, relief=SUNKEN)
label.pack(fill=tkinter.BOTH)

window.resizable(False, False)
window.mainloop()