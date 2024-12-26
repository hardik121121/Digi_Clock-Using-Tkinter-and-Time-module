from tkinter import Tk
from tkinter import Label
import time
import sys

root = Tk()
root.title("Digital Clock")

def present_time():
    display_time = time.strftime("%I:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200,present_time)

digi_clock = Label(root, font=("Ariral", 150), bg= "Light blue", fg="gray")
digi_clock.pack()

present_time()
root.mainloop()