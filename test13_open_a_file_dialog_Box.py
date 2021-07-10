# acknowledgement: Dr. Corey Schafer (youtube), Dr. John (codemy.com), Dr. Prakash Sharma

from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog  # for this function it is important to call it again like this; sepcify its name.
import os


def open_file():

    file = filedialog.askopenfile(initialdir=".",
                                           # set initial directory when the select window is popup; "." means current directory
                                           title="Please! select a file",  # set a title for the select window
                                           # filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*")),
                                           # set a filetype that you want to show or select, it doesn't work well on mac
                                           )

    # Note: filedialog will return a path, it is also embedded with other information.
    # So, we need to use the os.path.abspath(file.name) to get only the path information.

    file_path = os.path.abspath(file.name) # this function is used to return an absolute path

    img = Image.open(file_path)
    img.show()


window = Tk()

my_button = Button(window, text="Please! select an image file", command=open_file).pack(padx=20, pady=20)

window.mainloop()