# Acknowledgement: Dr John (codemy.com)
from tkinter import *

window1 = Tk()
window1.title("Window 1")


def new_window():
    window2 = Toplevel()        # to set a second window
    window2.title("New window")
    exit_button = Button(window2, text="Please! click me to exit this window.",
                         command=window2.destroy).pack(padx=20, pady=20)
    # destroy() is used to close the current window




open_new_window = Button(window1, text="Please! click me to see a new window.",
                         command= new_window).pack(padx=20, pady=10)
quit_button = Button(window1, text="Please! click me to quite the program.",
                     command=window1.quit).pack(padx=20, pady=10)













window1.mainloop()