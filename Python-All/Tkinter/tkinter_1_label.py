#!/usr/bin/python3

from tkinter import *

top = Tk()
top.geometry("450x300")

# the label for user_name

lbl_user_name = Label(top, text="User Name").place(x=40, y=60)

# the label for user_password

lbl_user_password = Label(top, text="User Password").place(x=40, y=100)

btn_submit_button = Button(top, text="Submit").place(x=40, y=130)

user_name_input_area = Entry(top, width=30).place(x=110, y=60)
user_password_entry_area = Entry(top, width=30).place(x=110, y=100)

top.mainloop()
