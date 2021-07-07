# Acknowledgement: Dr Angela Yu

from tkinter import *
from PIL import ImageTk, Image
from os import *

root = Tk()
# root.geometry("900x550")
root.title("Image viewer")

icon = Image.open("icon.jpg")
icon.save('griffith.ico',format = 'ICO', sizes=[(10,10)])
root.iconbitmap('griffith.ico')

img_list = []
n = 0
for img in listdir("./Wallpapers/jpg wallpapers"):
    i = Image.open(f"./Wallpapers/jpg wallpapers/{img}")
    i.thumbnail((900, 900))
    j = ImageTk.PhotoImage(i)
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
    else:
        n += 1
        img_viewer = Label(root, image=img_list[n])
        img_viewer.grid(row=0, column=0, columnspan=3)



def backward():
    global n
    global img_viewer
    img_viewer.grid_forget()
    if n == -(len(img_list)):
        n = (len(img_list)-1)
        img_viewer = Label(root, image=img_list[n])
        img_viewer.grid(row=0, column=0, columnspan=3)
    else:
        n -= 1
        img_viewer = Label(root, image=img_list[n])
        img_viewer.grid(row=0, column=0, columnspan=3)


backward_button = Button(root, text="<<", command=backward)
forward_button = Button(root, text=">>", command=forward)
exit_button = Button(root, text="Exit Viewer", command=root.quit)

backward_button.grid(row=2, column=0)
forward_button.grid(row=2, column=2)
exit_button.grid(row=2, column=1)


root.mainloop()