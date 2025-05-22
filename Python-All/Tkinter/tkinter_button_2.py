#!/usr/bin/python

# import tkinter module

from tkinter import *

"""Following will import tkinter.ttk module and
automatically override all the widgets
which are present in tkinter module."""

from tkinter.ttk import *

# Create Object
root = Tk()

# Initialize tkinter window with dimension 100x100
root.geometry("100x100")

btn = Button(root, text="Click me!", command=root.destroy)

# Set the position of Button on the top of Window
btn.pack(side="top")

root.mainloop()
