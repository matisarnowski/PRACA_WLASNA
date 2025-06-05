#!/usr/bin/python3

# Importing tkinter module
from tkinter import *

# from tkinter.ttk import *

# Creating master tkinter window
master = Tk()
master.geometry("175x175")

# Ikinter string variable
# able to store any string value
v = StringVar(master, "1")

# Dictionary to create multiple buttons
values = {
    "RadioButton 1": "1",
    "RadioButton 2": "2",
    "RadioButton 3": "3",
    "RadioButton 4": "4",
    "RadioButton 5": "5",
}

# Loop is used to create multiple Radiobuttons
# rather then creating each button separately
for text, value in values.items():
    Radiobutton(
        master, text=text, variable=v, value=value, indicator=0, background="light blue"
    ).pack(fill=X, pady=5)
# Infinite loop can be terminated by
# Keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()
