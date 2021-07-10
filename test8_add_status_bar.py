# Acknowledgement: Dr Angela Yu (udemy.com)
# Acknowledgement: Dr John (codemy.com)

# note: tkinter is about two processes. first, you do sth. then you show it on the screen or window

from tkinter import *
from PIL import ImageTk, Image
from os import *

root = Tk()
# root.geometry("900x550")


icon = Image.open("icon.jpg")
icon.save('griffith.ico',format = 'ICO', sizes=[(10,10)])
root.iconbitmap('griffith.ico')
root.title("Image viewer")

img_list = []
n = 0
for img in listdir("./Wallpapers/jpg wallpapers"):  #loops through directory
    i = Image.open(f"./Wallpapers/jpg wallpapers/{img}")    #open images first
    i.thumbnail((900, 900))     #change images size
    j = ImageTk.PhotoImage(i)   #need to use this funtion, or tkinter won't recognise the images
    img_list.append(j)

img_viewer = Label(root, image=img_list[n])
img_viewer.grid(row=0, column=0, columnspan=3)


def forward():
    global n
    global img_viewer
    img_viewer.grid_forget()

    if n == (len(img_list)-1):
        n = 0
        img_viewer = Label(root, image=img_list[n])
        img_viewer.grid(row=0, column=0, columnspan=3)
        status_bar = Label(root, text=f"Image{n+1}/{len(img_list)}", bd=1, relief=SUNKEN,
                           anchor=E)
        status_bar.grid(row=3, column=0, columnspan=3, sticky=W + E)
    else:
        n += 1
        img_viewer = Label(root, image=img_list[n])
        img_viewer.grid(row=0, column=0, columnspan=3)
        status_bar = Label(root, text=f"Image{n+1}/{len(img_list)}", bd=1, relief=SUNKEN,
                           anchor=E)
        status_bar.grid(row=3, column=0, columnspan=3, sticky=W + E)


def backward():
    global n
    global img_viewer
    img_viewer.grid_forget()
    if n == -(len(img_list)):
        n = (len(img_list)-1)
        img_viewer = Label(root, image=img_list[n])
        img_viewer.grid(row=0, column=0, columnspan=3)
        status_bar = Label(root, text=f"Image{n+1}/{len(img_list)}", bd=1, relief=SUNKEN,
                           anchor=E)
        status_bar.grid(row=3, column=0, columnspan=3, sticky=W + E)
    else:
        n -= 1
        img_viewer = Label(root, image=img_list[n])
        img_viewer.grid(row=0, column=0, columnspan=3)
        status_bar = Label(root, text=f"Image{n+1}/{len(img_list)}", bd=1, relief=SUNKEN,
                           anchor=E)
        status_bar.grid(row=3, column=0, columnspan=3, sticky=W + E)



backward_button = Button(root, text="<<", command=backward)
forward_button = Button(root, text=">>", command=forward)
exit_button = Button(root, text="Exit Viewer", command=root.quit)
status_bar = Label(root, text=f"Image{1}/{len(img_list)}", bd=1, relief=SUNKEN, anchor=E) # use anchor to set the
# alignment here.

backward_button.grid(row=2, column=0)
forward_button.grid(row=2, column=2)
exit_button.grid(row=2, column=1, pady=10) # add pady so that the status bar is not too close to row 2
status_bar.grid(row=3, column=0, columnspan=3, sticky=W+E) # sticky might be used to set the alignment; however, we use-
# it to stretch the border instead by using W+E as the arguments. to set the alignment use anchor in Label function.

root.mainloop()