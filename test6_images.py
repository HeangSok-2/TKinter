from tkinter import *
from PIL import ImageTk, Image

# tkinter accept only two type of image files (EX: gif); therefore, we use PIL to use more type of image file
root = Tk()
root.title('I am meow')

icon = 'totoro.jpg'
img = ImageTk.PhotoImage(Image.open(icon))
# icon= PhotoImage("totoro.jpg")
# root.iconbitmap(icon)

my_label = Label(root, image=img)
my_label.pack()


button_quit = Button(root, text= "Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()