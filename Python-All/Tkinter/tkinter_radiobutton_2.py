#!/usr/bin/python3
# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *

# Creating master tkinter window
master = Tk()
master.geometry("175x175")

# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")
# Style class to add style to RadioButton
# It can be used to style any ttk widgets
style = Style(master)
style.configure(
    "TRadiobutton",
    background="light green",
    foreground="red",
    font=("arial", 10, "bold"),
)
# Dictionary to Create multple buttons
values = {
    "RadioButton 1": "1",
    "RadioButton 2": "2",
    "RadioButton 3": "3",
    "RadioButton 4": "4",
    "RadioButton 5": "5",
}

# Loop is used to create multiple RadioButtons
# rathert than creating eaxch button separately
for text, value in values.items():
    Radiobutton(master, text=text, variable=v, value=value).pack(side=TOP, ipady=5)
# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()
