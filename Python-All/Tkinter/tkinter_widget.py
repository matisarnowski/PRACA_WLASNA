#!/usr/bin/python3

from tkinter import *

# tworzenie okna root
root = Tk()
# ramka wewnątrz okna root
frame = Frame(root)
# metoda rozmieszczająca
frame.pack()
# przycisk wewnątrz ramki, która jest wewnątrz okna root
button = Button(frame, text="Geek")
button.pack()
# Ostateczna pętla tkintera
root.mainloop()
