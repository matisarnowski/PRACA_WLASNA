#!/usr/bin/python3

from tkinter import *
from szyfr_solitare import *


def entry_string():
    string_a.set(writing_encrypt(writing.get()))


window = Tk()
window.title("Wprowadź tekst!")
writing = StringVar()
string_a = StringVar()

label = Label(window, text="Podaj tekst do zaszyfrowania: ").grid(row=0, column=0)
text = Entry(window, textvariable=writing).grid(row=0, column=1)
button = Button(window, text="Zaszyfruj!", command=entry_string).grid(row=1, column=0)
label_finish = Label(window, textvariable=string_a).grid(row=1, column=1)
window.mainloop()
