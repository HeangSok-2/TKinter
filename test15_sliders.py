# Acknowledgement: Bro code (youtube)

from tkinter import *

window = Tk()


def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")


scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=HORIZONTAL,  # orientation of scale; you can change to HORIZONTAL if you want
              font=('Consolas', 20),
              tickinterval=10,  # adds numeric indicators for value
              # showvalue = 0,   # hide current value when sliding
              resolution=5,  # increment of slider
              troughcolor='#69EAFF',  # slider color
              fg='#FF1C00',  # font color
              bg='#111111'  # background color

              )
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])  # set current value of slider

scale.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()

window.mainloop()
